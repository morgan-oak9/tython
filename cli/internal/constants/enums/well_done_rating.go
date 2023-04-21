package enums

type WellDoneRating struct {
	value string
}

func (wd WellDoneRating) String() string {
	return wd.value
}

var (
	WellDoneRatingOk      WellDoneRating = WellDoneRating{"Ok"}
	WellDoneRatingGood    WellDoneRating = WellDoneRating{"Good"}
	WellDoneRatingGreat   WellDoneRating = WellDoneRating{"Great"}
	WellDoneRatingAmazing WellDoneRating = WellDoneRating{"Amazing"}
)
