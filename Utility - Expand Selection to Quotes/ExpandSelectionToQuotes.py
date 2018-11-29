import sublime, sublime_plugin

class ExpandSelectionToQuotesCommand(sublime_plugin.TextCommand):
    def description(self):
        return 'Expand Selection to String Quotes'

    def run(self, edit):
        strings = self.view.find_by_selector('string')
        for selection in self.view.sel():
            selection_start = selection.begin();

            for string in strings:
                start = string.begin() + 1;
                end = string.end() - 1;

                if selection_start > string.begin() and selection_start < string.end():
                    if selection.size() == (end - start):
                        start = string.begin();
                        end = string.end();

                    self.view.sel().subtract(selection)
                    self.view.sel().add(sublime.Region(start, end))
