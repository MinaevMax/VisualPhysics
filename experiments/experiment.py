from multiprocessing import Process
import i18n


class Experiment(Process):
    def __init__(self):
        """Init.

            Initializing the base.
        """
        super().__init__()

    def _init_i18n(self):
        """i18n

            Initializing the localized text.
        """
        import locale

        match locale.getlocale()[0]:
            case locale if 'ru' in locale.lower():
                i18n.set('locale', 'ru')
            case _:
                i18n.set('locale', 'en')

        i18n.resource_loader.init_json_loader()
        i18n.set('filename_format', '{locale}.{format}')
        i18n.set('file_format', 'json')
        i18n.set('skip_locale_root_data', True)
        i18n.set('enable_memoization', True)
        i18n.load_path.append('assets/locales/')
