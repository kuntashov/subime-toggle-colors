import sublime
import sublime_plugin


class ToggleColorsCommand(sublime_plugin.TextCommand):

    def run(self, edit, **args):

        self.dark = args["dark_colors"]
        self.light = args["light_colors"]

        self.settings_file = "Preferences.sublime-settings"

        self.toggle_colors()

    def toggle_colors(self):
        new_colors = self.dark if self.is_light() else self.light
        self.set_colors(new_colors)

    def is_light(self):
        settings = sublime.load_settings(self.settings_file)
        current_scheme = settings.get("color_scheme")
        return current_scheme == self.light['color_scheme']

    def set_colors(self, colors):
        settings = sublime.load_settings(self.settings_file)
        settings.set("color_scheme", colors["color_scheme"])
        settings.set("theme", colors["theme"])
        settings.save_settings(self.settings_file)
