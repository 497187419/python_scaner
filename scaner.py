import twain
import os

# 初始化驱动
sm = twain.SourceManager(0)
# 打开指定设备
ss = sm.OpenSource()
# ss = sm.OpenSource('<扫描仪设备名>')
try:
	# 请求设备开始扫描，唤醒设备
	ss.RequestAcquire(0, 0)
except:
	print('取消扫描')
	os._exit(0)

# 尝试捕捉1千次扫描回调结果
for x in range(1,1001):
	# 尝试执行扫描
	try:
		# 获取扫描结果
		rv = ss.XferImageNatively()
	except:
		print('扫描完成')
		break
	# 如果有内容（非空白）
	if rv:
		# 拆解结果
		(handle, count) = rv
		# 保存图片
		twain.DIBToBMFile(handle, str(x)+'.bmp')
		# 释放内存
		twain.GlobalHandleFree(handle)
		# 获取该轮扫描张数
		page_count = x
print('共扫描'+ str(page_count) +'张')