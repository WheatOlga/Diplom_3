class Urls:
    BASE_URL = "https://qa-stellarburgers.education-services.ru"

    HOME_URL = BASE_URL
    LOGIN_URL = BASE_URL + "/login"
    FORGOT_PASSWORD_URL = BASE_URL + "/forgot-password"
    RESET_PASSWORD_URL = BASE_URL + "/reset-password"
    CREATE_USER = BASE_URL + "/api/auth/register"
    DELETE_USER = BASE_URL + "/api/auth/user"
    ORDER_HISTORY_URL = BASE_URL + "/account/order-history"
    PROFILE_URL = BASE_URL + "/account"
    CONSTRUCTOR_URL = BASE_URL + "/"
    FEED_URL = BASE_URL + "/feed"

    CONTAINS_ACCOUNT = "/account"
    CONTAINS_ORDER_HISTORY = "/account/order-history"
    CONTAINS_LOGIN = "/login"
    CONTAINS_REGISTER = "/register"
    