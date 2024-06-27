class SmtpEmailService:
    def send_email(self, email_list, content):
        print(f"Sending email to {email_list}: {content}")

class ApiCryptoDataService:
    def get_crypto_data(self):
        return {
            "price": "50000",
            "volume": "1000",
            "high": "51000",
            "market_cap": "900B"
        }
