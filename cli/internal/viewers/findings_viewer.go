package viewers

import (
	"fmt"
	"io"
	"strconv"
	"strings"

	"oak9.io/tython/internal/constants/enums"
	"oak9.io/tython/internal/models/runner"
	"oak9.io/tython/internal/visuals"
)

const (
	CriticalFindingsRowTitle string = "critical findings"
	HighFindingsRowTitle     string = "high findings"
	ModerateFindingsRowTitle string = "moderate findings"
	LowFindingsRowTitle      string = "low findings"
	KudosFindingsRowTitle    string = "kudos"
	TotalRowTitle            string = "total"
)

type FindingsViewer struct {
	Findings []runner.Finding
}

func (viewer FindingsViewer) View(writers ...io.Writer) error {
	err := visuals.SkipNLines(1, writers...)
	if err != nil {
		return err
	}

	if err := visuals.DrawSectionSeparatorWithTitle("Findings", writers...); err != nil {
		return err
	}

	if len(viewer.Findings) == 0 {
		return visuals.WriteLine("No findings were reported!", writers...)
	}

	counts := make(map[string]int, 0)

	rows := []string{
		CriticalFindingsRowTitle,
		HighFindingsRowTitle,
		ModerateFindingsRowTitle,
		LowFindingsRowTitle,
		KudosFindingsRowTitle,
		TotalRowTitle,
	}

	for _, rowname := range rows {
		counts[rowname] = 0
	}

	groupedFindings := viewer.groupByReqName()

	for reqName, findingList := range groupedFindings {
		visuals.WriteTitle(fmt.Sprintln(reqName), writers...)
		for _, finding := range findingList {
			visuals.WriteSubTitle(
				fmt.Sprintf("%s%s%s", finding.Rating, strings.Repeat(" ", visuals.IndentLength), finding.Desc),
				writers...,
			)
			visuals.SkipNLines(1, writers...)

			countSeverity(finding, counts)
			countKudos(finding, counts)
		}
	}

	visuals.DrawSectionSeparator(writers...)

	total := 0
	stringCounts := make(map[string]string, len(counts))

	for key, count := range counts {
		total = total + count
		stringCounts[key] = strconv.Itoa(count)
	}
	stringCounts[TotalRowTitle] = strconv.Itoa(total)

	if err := visuals.DrawSimpleOrderedKeyValueTable(stringCounts, rows, writers...); err != nil {
		visuals.WriteSubTitle("There was an issue displaying the summary table", writers...)
		return err
	}

	visuals.SkipNLines(2, writers...)

	return nil
}

func (viewer FindingsViewer) groupByReqName() (groupedFindings map[string][]runner.Finding) {
	groupedFindings = make(map[string][]runner.Finding, 0)

	for _, finding := range viewer.Findings {
		if findingList, exists := groupedFindings[finding.ReqName]; exists {
			groupedFindings[finding.ReqName] = append(findingList, finding)
		} else {
			groupedFindings[finding.ReqName] = []runner.Finding{finding}
		}
	}

	return
}

func countSeverity(finding runner.Finding, counts map[string]int) {
	switch finding.Rating {
	case enums.SeverityCritical.String():
		counts[CriticalFindingsRowTitle]++
	case enums.SeverityHigh.String():
		counts[HighFindingsRowTitle]++
	case enums.SeverityModerate.String():
		counts[ModerateFindingsRowTitle]++
	case enums.SeverityLow.String():
		counts[LowFindingsRowTitle]++
	default:

	}
}

func countKudos(finding runner.Finding, counts map[string]int) {
	switch finding.Rating {
	case enums.WellDoneRatingOk.String():
		fallthrough
	case enums.WellDoneRatingGood.String():
		fallthrough
	case enums.WellDoneRatingGreat.String():
		fallthrough
	case enums.WellDoneRatingAmazing.String():
		counts[KudosFindingsRowTitle]++
	default:

	}
}
