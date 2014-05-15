    # http://www.daniweb.com/software-development/python/code/216752/yac-wxpython-tiny-calculator
	# yet another calculator, a wxPython tiny calculator that is ...
    # tested with Python24 vegaseat 08jul2006
    
import wx
    
class MyFrame(wx.Frame):
		"""make a frame, inherits wx.Frame"""
		def __init__(self):
			# create a frame/window, no parent, default to wxID_ANY or -1
			wx.Frame.__init__(self, None, wx.ID_ANY, 'wxCalc', pos=(300, 150), size=(185, 200))
			self.SetBackgroundColour('green')
			self.edit1 = wx.TextCtrl(self, -1, value="", pos=(5,5), size=(165, 25))
			
			# now create all the buttons and bind the event
			self.btn_0 = wx.Button(self, -1, label='0', pos=(5, 130), size=(20, 20))
			self.btn_0.Bind(wx.EVT_BUTTON, self.btn_0Click)
			
			self.btn_p = wx.Button(self, -1, label='.', pos=(35, 130), size=(20, 20))
			self.btn_p.Bind(wx.EVT_BUTTON, self.btn_pClick)
			
			self.btn_e = wx.Button(self, -1, label='=', pos=(65, 130), size=(20, 20))
			self.btn_e.Bind(wx.EVT_BUTTON, self.btn_eClick)
			
			self.btn_a = wx.Button(self, -1, label='+', pos=(105, 130), size=(20, 20))
			self.btn_a.Bind(wx.EVT_BUTTON, self.btn_aClick)
			
			self.btn_ng = wx.Button(self, -1, label='neg', pos=(135, 130), size=(30, 20))
			self.btn_ng.Bind(wx.EVT_BUTTON, self.btn_ngClick)
			
			self.btn_1 = wx.Button(self, -1, label='1', pos=(5, 100), size=(20, 20))
			self.btn_1.Bind(wx.EVT_BUTTON, self.btn_1Click)
			
			self.btn_2 = wx.Button(self, -1, label='2', pos=(35, 100), size=(20, 20))
			self.btn_2.Bind(wx.EVT_BUTTON, self.btn_2Click)
			
			self.btn_3 = wx.Button(self, -1, label='3', pos=(65, 100), size=(20, 20))
			self.btn_3.Bind(wx.EVT_BUTTON, self.btn_3Click)
			
			self.btn_s = wx.Button(self, -1, label='-', pos=(105, 100), size=(20, 20))
			self.btn_s.Bind(wx.EVT_BUTTON, self.btn_sClick)
			
			self.btn_mm = wx.Button(self, -1, label='**', pos=(135, 100), size=(30, 20))
			self.btn_mm.Bind(wx.EVT_BUTTON, self.btn_mmClick)
			self.btn_mm.SetToolTip(wx.ToolTip('power'))
			
			self.btn_4 = wx.Button(self, -1, label='4', pos=(5, 70), size=(20, 20))
			self.btn_4.Bind(wx.EVT_BUTTON, self.btn_4Click)
			
			self.btn_5 = wx.Button(self, -1, label='5', pos=(35, 70), size=(20, 20))
			self.btn_5.Bind(wx.EVT_BUTTON, self.btn_5Click)
			
			self.btn_6 = wx.Button(self, -1, label='6', pos=(65, 70), size=(20, 20))
			self.btn_6.Bind(wx.EVT_BUTTON, self.btn_6Click)
			
			self.btn_m = wx.Button(self, -1, label='*', pos=(105, 70), size=(20, 20))
			self.btn_m.Bind(wx.EVT_BUTTON, self.btn_mClick)
			
			self.btn_b = wx.Button(self, -1, label='<-', pos=(135, 70), size=(30, 20))
			self.btn_b.Bind(wx.EVT_BUTTON, self.btn_bClick)
			self.btn_b.SetToolTip(wx.ToolTip('backspace'))
			
			self.btn_7 = wx.Button(self, -1, label='7', pos=(5, 40), size=(20, 20))
			self.btn_7.Bind(wx.EVT_BUTTON, self.btn_7Click)
			
			self.btn_8 = wx.Button(self, -1, label='8', pos=(35, 40), size=(20, 20))
			self.btn_8.Bind(wx.EVT_BUTTON, self.btn_8Click)
			
			self.btn_9 = wx.Button(self, -1, label='9', pos=(65, 40), size=(20, 20))
			self.btn_9.Bind(wx.EVT_BUTTON, self.btn_9Click)
			
			self.btn_d = wx.Button(self, -1, label='/', pos=(105, 40), size=(20, 20))
			self.btn_d.Bind(wx.EVT_BUTTON, self.btn_dClick)
			
			self.btn_c = wx.Button(self, -1, label='c', pos=(135, 40), size=(20, 20))
			self.btn_c.Bind(wx.EVT_BUTTON, self.btn_cClick)
			self.btn_c.SetToolTip(wx.ToolTip('clear entry'))
			
			# show the frame
			self.Show(True)
		
		def btn_0Click(self, event):
			self.edit1.SetValue(self.edit1.GetValue() + '0')
    
		def btn_pClick(self, event):
			self.edit1.SetValue(self.edit1.GetValue() + '.')
    
		def btn_eClick(self, event):
			"""equal"""
			str1 = self.edit1.GetValue()
    
			while str1[0] == '0':
				# avoid leading zero (octal) error with eval()
				str1 = str1[1:]
			if '/' in str1 and '.' not in str1:
				# turn into floating point division
				str1 = str1 + '.0'
			try:
				self.edit1.SetValue(str(eval(str1)))
			except ZeroDivisionError:
				self.edit1.SetValue('division by zero error')
    
		def btn_aClick(self, event):
			self.edit1.SetValue(self.edit1.GetValue() + '+')
    
		def btn_ngClick(self, event):
			self.edit1.SetValue('-' + self.edit1.GetValue())
    
		def btn_1Click(self, event):
			self.edit1.SetValue(self.edit1.GetValue() + '1')
    
		def btn_2Click(self, event):
			self.edit1.SetValue(self.edit1.GetValue() + '2')
    
		def btn_3Click(self, event):
			self.edit1.SetValue(self.edit1.GetValue() + '3')
    
		def btn_sClick(self, event):
			self.edit1.SetValue(self.edit1.GetValue() + '-')
    
		def btn_mmClick(self, event):
			"""power"""
			self.edit1.SetValue(self.edit1.GetValue() + '**')
    
		def btn_4Click(self, event):
			self.edit1.SetValue(self.edit1.GetValue() + '4')
    
		def btn_5Click(self, event):
			self.edit1.SetValue(self.edit1.GetValue() + '5')
    
		def btn_6Click(self, event):
			self.edit1.SetValue(self.edit1.GetValue() + '6')
    
		def btn_mClick(self, event):
			self.edit1.SetValue(self.edit1.GetValue() + '*')
    
		def btn_7Click(self, event):
			self.edit1.SetValue(self.edit1.GetValue() + '7')
    
		def btn_8Click(self, event):
			self.edit1.SetValue(self.edit1.GetValue() + '8')
    
		def btn_9Click(self, event):
			self.edit1.SetValue(self.edit1.GetValue() + '9')
    
		def btn_dClick(self, event):
			self.edit1.SetValue(self.edit1.GetValue() + '/')
    
		def btn_cClick(self, event):
			"""clear"""
			self.edit1.SetValue('')
    
		def btn_bClick(self, event):
			"""backspace"""
			self.edit1.SetValue(self.edit1.GetValue()[:-1])
    
application = wx.PySimpleApp()
# call class MyFrame
window = MyFrame()
# start the event loop
application.MainLoop()

