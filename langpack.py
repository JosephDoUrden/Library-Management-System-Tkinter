# Supports both hardcoded language strings and external language files.

import glob


class I18N:
    def __init__(self, language, load_from_file=True):
        if language in self.get_available_languages():
            self.load_data_from_file(language)
        else:
            raise NotImplementedError("Unsupported language. Add missing language file.")

    def load_data_from_file(self, lang):
        lang_data = {}
        lang_file = f"data_{lang}.lng"
        with open(file=lang_file, encoding="utf-8") as f:
            for line in f:
                key, val = line.strip().split("=")
                lang_data[key] = val

        self.message_username_error = lang_data["message_username_error"]
        self.message_username_exist = lang_data["message_username_exist"]
        self.message_password_error = lang_data["message_password_error"]
        self.message_role_error = lang_data["message_role_error"]
        self.message_email_error = lang_data["message_email_error"]
        self.message_phone_error = lang_data["message_phone_error"]
        self.message_save_success_user = lang_data["message_save_success_user"]
        self.message_save_error_user = lang_data["message_save_error_user"]
        self.message_title_error = lang_data["message_title_error"]
        self.message_author_error = lang_data["message_author_error"]
        self.message_genre_error = lang_data["message_genre_error"]
        self.message_publication_year_error = lang_data["message_publication_year_error"]
        self.message_isbn_error = lang_data["message_isbn_error"]
        self.message_status_error = lang_data["message_status_error"]
        self.message_status_value_error = lang_data["message_status_value_error"]
        self.message_save_success_book = lang_data["message_save_success_book"]
        self.message_save_error_book = lang_data["message_save_error_book"]
        self.message_database_create_success = lang_data["message_database_create_success"]
        self.message_database_create_error = lang_data["message_database_create_error"]
        self.message_database_fill_success = lang_data["message_database_fill_success"]
        self.message_database_fill_error = lang_data["message_database_fill_error"]
        self.message_database_clear_success = lang_data["message_database_clear_success"]
        self.message_database_clear_error = lang_data["message_database_clear_error"]
        self.message_confirm_delete = lang_data["message_confirm_delete"]
        self.message_error_text = lang_data["message_error_text"]
        self.text_username = lang_data["text_username"]
        self.text_password = lang_data["text_password"]
        self.text_role = lang_data["text_role"]
        self.text_email = lang_data["text_email"]
        self.text_phone = lang_data["text_phone"]
        self.text_save_button_user = lang_data["text_save_button_user"]
        self.text_title = lang_data["text_title"]
        self.text_author = lang_data["text_author"]
        self.text_genre = lang_data["text_genre"]
        self.text_publication_year = lang_data["text_publication_year"]
        self.text_isbn = lang_data["text_isbn"]
        self.text_status = lang_data["text_status"]
        self.text_available_copies = lang_data["text_available_copies"]
        self.text_total_copies = lang_data["text_total_copies"]
        self.text_save_button_book = lang_data["text_save_button_book"]
        self.text_create_database_button = lang_data["text_create_database_button"]
        self.text_fill_database_button = lang_data["text_fill_database_button"]
        self.text_clear_database_button = lang_data["text_clear_database_button"]
        self.text_add_new_button_book = lang_data["text_add_new_button_book"]
        self.text_show_list_button = lang_data["text_show_list_button"]
        self.text_add_new_button_user = lang_data["text_add_new_button_user"]
        self.text_id_column = lang_data["text_id_column"]
        self.text_title_column = lang_data["text_title_column"]
        self.text_author_column = lang_data["text_author_column"]
        self.text_genre_column = lang_data["text_genre_column"]
        self.text_publication_year_column = lang_data["text_publication_year_column"]
        self.text_isbn_column = lang_data["text_isbn_column"]
        self.text_status_column = lang_data["text_status_column"]
        self.text_user_id_column = lang_data["text_user_id_column"]
        self.message_invalid_status = lang_data["message_invalid_status"]
        self.text_title_book = lang_data["text_title"]
        self.text_author_book = lang_data["text_author"]
        self.text_genre_book = lang_data["text_genre"]
        self.text_publication_year_book = lang_data["text_publication_year"]
        self.text_isbn_book = lang_data["text_isbn"]
        self.text_status_book = lang_data["text_status"]
        self.text_update_book = lang_data["text_update_book"]
        self.message_failed_update_user = lang_data["message_failed_update_user"]
        self.text_update_user = lang_data["text_update_user"]
        self.text_login = lang_data["text_login"]
        self.text_close = lang_data["text_close"]
        self.text_admin = lang_data["text_admin"]
        self.text_user = lang_data["text_user"]
        self.title_login_window = lang_data["title_login_window"]
        self.message_confirm_delete_user = lang_data["message_confirm_delete"]
        self.text_user_list = lang_data["text_user_list"]
        self.text_confirm_delete = lang_data["text_confirm_delete"]
        self.text_id_user = lang_data["text_id"]
        self.text_role_user = lang_data["text_role"]
        self.text_username_user = lang_data["text_username"]
        self.text_password_user = lang_data["text_password"]
        self.text_email_user = lang_data["text_email"]
        self.text_phone_user = lang_data["text_phone"]
        self.title_user_edit_window = lang_data["title_user_edit_window"]
        self.message_confirm_borrow = lang_data["message_confirm_borrow"]
        self.message_confirm_return = lang_data["message_confirm_return"]
        self.text_user_tab = lang_data["text_user"]
        self.text_library_tab = lang_data["text_library"]
        self.text_my_books_tab = lang_data["text_my_books"]
        self.text_profile_tab = lang_data["text_profile"]
        self.text_username_profile = lang_data["text_username"]
        self.text_role_profile = lang_data["text_role"]
        self.text_email_profile = lang_data["text_email"]
        self.text_phone_profile = lang_data["text_phone"]
        self.title_change_password = lang_data["title_change_password"]
        self.text_old_password = lang_data["text_old_password"]
        self.text_new_password = lang_data["text_new_password"]
        self.message_confirm_change_password = lang_data["message_confirm_change_password"]
        self.message_confirm_change_password_success = lang_data["message_confirm_change_password_success"]
        self.message_confirm_change_password_fail = lang_data["message_confirm_change_password_fail"]
        self.message_confirm_change_password_incorrect_old = lang_data["message_confirm_change_password_incorrect_old"]
        self.message_save_error_book_new = lang_data["message_save_error_book_new"]
        self.text_issued = lang_data["text_issued"]
        self.message_confirm_change_fail = lang_data["message_confirm_change_fail"]


    @staticmethod
    def get_available_languages():
        language_files = glob.glob("data_*.lng")
        language_codes = [f.replace("data_", "").replace(".lng", "") for f in language_files]
        return language_codes
