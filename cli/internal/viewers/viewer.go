package viewers

import "io"

type Viewer interface {
	View(writers ...io.Writer) error
}
