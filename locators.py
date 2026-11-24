from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт» на главной
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка «Личный кабинет» в шапке
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка «Конструктор» в шапке
    LOGO_BUTTON = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")  # Логотип Stellar Burgers в шапке
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка «Оформить заказ» (появляется после входа)

    # Вкладки разделов конструктора
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")  # Вкладка «Булки» в конструкторе
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")  # Вкладка «Соусы» в конструкторе
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")  # Вкладка «Начинки» в конструкторе


class LoginPageLocators:
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")  # Заголовок формы входа «Вход»
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле ввода Email на странице входа
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле ввода Пароля на странице входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка «Войти» в форме входа


class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле ввода «Имя» при регистрации
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле ввода «Email» при регистрации
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле ввода «Пароль» при регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка «Зарегистрироваться»
    PASSWORD_ERROR_TEXT = (By.XPATH, "//p[text()='Некорректный пароль']")  # Сообщение об ошибке «Некорректный пароль»
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка «Войти» внизу формы регистрации


class ForgotPasswordPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка «Войти» в форме восстановления пароля


class ProfilePageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка «Выход» в личном кабинете
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")  # Вкладка «Профиль» в личном кабинете
