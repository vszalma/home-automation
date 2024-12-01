import hashlib
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from mailersend import emails


def _calculate_file_hash(file_path, hash_algorithm="sha256"):
    try:
        # Create a hash object
        hash_func = hashlib.new(hash_algorithm)
        # Read the file in chunks to handle large files
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):  # Read in 8KB chunks
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        raise Exception(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error calculating hash: {e}")


def compare_files(file1, file2, hash_algorithm="sha256"):
    try:
        hash1 = _calculate_file_hash(file1, hash_algorithm)
        hash2 = _calculate_file_hash(file2, hash_algorithm)
        return hash1 == hash2
    except Exception as e:
        print(f"Error comparing files: {e}")
        return False


def get_arguments(argv):
    arg_help = "{0} <file1> <file2>".format(argv[0])

    try:
        file1 = (
            sys.argv[1]
            if len(sys.argv) > 1
            else '"C:\\Users\\vszal\\OneDrive\\Pictures"'
        )
        file2 = sys.argv[2] if len(sys.argv) > 2 else "image"
    except:
        print(arg_help)
        sys.exit(2)

    return [file1, file2]

from mailersend import emails

def send_email(subject, body):
    try:

        mailer = emails.NewEmail("mlsn.011b4017977722058e2195d23680a996ed8e5204da1922fefe9e8e23a30bbc2f")

        mail_body = {}

        mail_from = {
            "name": "me",
            "email": "MS_eLLyva@trial-x2p034766dkgzdrn.mlsender.net",
        }

        recipients = [
            {
                "name": "Victor Szalma",
                "email": "vszalma@hotmail.com",
            }
        ]

        reply_to = {
            "name": "Victor Szalma",
            "email": "vszalma@hotmail.com",
        }

        mailer.set_mail_from(mail_from, mail_body)
        mailer.set_mail_to(recipients, mail_body)
        mailer.set_subject(subject, mail_body)
        mailer.set_html_content(body, mail_body)
        mailer.set_plaintext_content(body, mail_body)
        mailer.set_reply_to(reply_to, mail_body)

        # using print() will also return status code and data
        mailer.send(mail_body)
            

        print(f"Email sent to {recipients}")
        
    except Exception as e:
        print(f"Error sending email: {e}")





if __name__ == "__main__":
    arguments = get_arguments(sys.argv)
    print("File to be compared (1): ", arguments[0])
    print("File to be compared (2): ", arguments[1])

    if compare_files(arguments[0], arguments[1]):
        print("The files are identical.")
    else:
        print("The files are different.")

    send_email(
        subject="Test Email from Python",
        body="This is a test email.",
        to_email="vszalma@hotmail.com",
        from_email="vszalma@hotmail.com"
    )
