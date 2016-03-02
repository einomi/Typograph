import sublime, sublime_plugin

from .RemoteTypograf import RemoteTypograf

class TypographCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		typograph = RemoteTypograf('windows-1251')
		typograph.htmlEntities()
		typograph.br(0)
		typograph.p(0)
		typograph.nobr(3)
		for region in self.view.sel():
			regionText = self.view.substr(region)
			processed = typograph.processText(regionText).strip(' \n\r')
			self.view.replace(edit, region, processed)
