package sensor

import "context"

type Context struct {
	Ctx context.Context
}

type Result struct {
	CapFilePath string `json:"cap_file_path"`
}

// Sensor 探测器的定义
type Sensor interface {

	// IsCanRun 判断当前环境是否能够运行探测器
	IsCanRun(context *Context) (bool, error)

	// Run 运行探测器
	Run(ctx *Context) (*Result, error)

}

