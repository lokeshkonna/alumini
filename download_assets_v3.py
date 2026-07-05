import urllib.request
import os

API_KEY = os.getenv("GCP_API_KEY")

def download(url, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    print(f"Downloading {url} to {path}...")
    try:
        req = urllib.request.Request(url)
        # Using the key as a header as suggested by user's JSON
        req.add_header("X-Goog-Api-Key", API_KEY)
        # Also try as a Bearer token if it looks like one, but the JSON said X-Goog-Api-Key
        
        with urllib.request.urlopen(req) as response:
            with open(path, "wb") as f:
                f.write(response.read())
        print("Done.")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

assets = [
    ("https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzdkNzA4ZGZiOWZjYjQ4NDU5OTA4N2Q3MWFmMTI4Zjg5EgsSBxCrrtycwQYYAZIBIwoKcHJvamVjdF9pZBIVQhM2NzkxMzQ0NTc1ODQ1MTQ5MTMw&filename=&opi=89354086", "members/templates/stitch/events.html"),
    ("https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzQwYzYwYWJlYTljYTQ5N2M4ZTgzODE1NTM2Mzk5YjFhEgsSBxCrrtycwQYYAZIBIwoKcHJvamVjdF9pZBIVQhM2NzkxMzQ0NTc1ODQ1MTQ5MTMw&filename=&opi=89354086", "members/templates/stitch/posts_feed.html"),
    ("https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sX2U1MjJmY2Y0M2E2ODRhN2RhNDM4YjZjYjViMWZkNWJjEgsSBxCrrtycwQYYAZIBIwoKcHJvamVjdF9pZBIVQhM2NzkxMzQ0NTc1ODQ1MTQ5MTMw&filename=&opi=89354086", "members/templates/stitch/mentorship.html"),
    ("https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sX2U3OWFkYmY0NjU1YTRkMDliMDA2MGRmYzg4N2YzMWUyEgsSBxCrrtycwQYYAZIBIwoKcHJvamVjdF9pZBIVQhM2NzkxMzQ0NTc1ODQ1MTQ5MTMw&filename=&opi=89354086", "members/templates/stitch/profiles.html"),
    ("https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sX2Y1YjU2ZTlhNDFhMDQ0NzhiMzBiYjFhYmY2YjEyODgzEgsSBxCrrtycwQYYAZIBIwoKcHJvamVjdF9pZBIVQhM2NzkxMzQ0NTc1ODQ1MTQ5MTMw&filename=&opi=89354086", "members/templates/stitch/signup.html"),
    ("https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzVlMmM5YjIyNWZiNTRjZTg4NDU1NTVmMzMxMWMzMThkEgsSBxCrrtycwQYYAZIBIwoKcHJvamVjdF9pZBIVQhM2NzkxMzQ0NTc1ODQ1MTQ5MTMw&filename=&opi=89354086", "members/templates/stitch/home_page.html"),
    ("https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sX2U2YjdkMWIzZWY5YzQ0YmI5MzI2YzMzZDkxN2I4ZjE3EgsSBxCrrtycwQYYAZIBIwoKcHJvamVjdF9pZBIVQhM2NzkxMzQ0NTc1ODQ1MTQ5MTMw&filename=&opi=89354086", "members/templates/stitch/login.html"),
    ("https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sX2U4NjQ0NWQ0Y2RmMjQ5MDBhOThlOTQzMjliNGRhZWJmEgsSBxCrrtycwQYYAZIBIwoKcHJvamVjdF9pZBIVQhM2NzkxMzQ0NTc1ODQ1MTQ5MTMw&filename=&opi=89354086", "members/templates/stitch/dashboard.html"),
    ("https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwNzQ4MWZmZTg2MDQyYWRhMzIzYjgzMjViYTg5OGJjEgsSBxCrrtycwQYYAZIBIwoKcHJvamVjdF9pZBIVQhM2NzkxMzQ0NTc1ODQ1MTQ5MTMw&filename=&opi=89354086", "members/templates/stitch/jobs.html"),
    ("https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzJmYjMzNjM1NmI4MTQ5MzdhYWUzOWEyZDU5ODZkYzYxEgsSBxCrrtycwQYYAZIBIwoKcHJvamVjdF9pZBIVQhM2NzkxMzQ0NTc1ODQ1MTQ5MTMw&filename=&opi=89354086", "members/templates/stitch/messages.html"),
    ("https://lh3.googleusercontent.com/aida/ADBb0ujsLq7GXDXDgS5v-_A3hXJWqFMhM4s17jnYYggw7pelVy6FqsGKisl6FH2C5c0molNn6cJD5cUo57vR3eTEoptzH2_kP5475nqUpV3hXSd5CCmr1dJoyvDroxvI_jdxqJ8icwdVM35PkuProgIs7qA767e6U1-dQU9Lac2lgo2qxVc9hkn4tAHlgkFB9JXPtNGY4x0jfHr9AOjA39Q7JP7njoRFS-rmKEZpIyQCZPmSusf6PKywcOtyeIc", "members/static/members/img/stitch/events.png"),
    ("https://lh3.googleusercontent.com/aida/ADBb0ugq0E4ckQhYWzANG0zngJpJT_pCn8VikRU9F0xxH5uEBzIZYKRg8yOIXNJvVxwe43CiyhQHmdqjqa9plQAm-_oWCf5wtYYyNcON6pERUOuuGHBBJlbklsxkKhKE8fnQKYIEfIo21M-RjWcalXAah-1npwKPBwiH8tFIwlnSxkjNEQm7MPrTDtP9kVQAmRXTIjZ6bIOZ3dGKokmOjLjpbnCXo4lqu8zgs1FgEzGDEdlnbF4r_dNq2lhmoeM", "members/static/members/img/stitch/posts_feed.png"),
    ("https://lh3.googleusercontent.com/aida/ADBb0uiwjV0BWahyXrv_t3Kpe7vQZdyFPcIVyEW6tVXKxZbS85QfJCLvSMpodIeadwhRuLMed1u7QrsaWUGSgoj3WNCNFLp2kd19B3Ky7JROjSREgBu4I1dNpqainRrsKhNZulWbb9OSMa04_4mMjM0ZpNiMKYNjv-9Hfctj2_U2EJrI7gmKcImlT7R2C0HlRbRGzIN_cFsHNkZfhmPIUQEyynPvxZT7jrtXdEJjDq-3mIDo1J82JvSV1t9SqXE", "members/static/members/img/stitch/mentorship.png"),
    ("https://lh3.googleusercontent.com/aida/ADBb0ugHZj4JQy7Th3QXhK3IPyxLDgqMXJDUhLTZKQZusk0m2uNo_yFGh3H-XE_b_tRsvGDwGLqP9j0tgsEbhPluPGLlCw-FdEK4LER3WMdn1w8FMTlqaHDxfv-Sj2eOAeZnHbpdtr1YexRI84o0THFl6O3Cy3hi1e6TrfNndkdUOhl6S4E-HiF_2wf3q4ZzlLpj09DdAhyyA15-x9cbRHKxcEFIhRglfENMa-FEeOLplz0GRYGyED6ft357q3o", "members/static/members/img/stitch/profiles.png"),
    ("https://lh3.googleusercontent.com/aida/ADBb0ug_XIqO9o4sWJF9p_xcBVoi7Fset-bjldSnkrNLmNnwQjuFEq5UWfuri_e4psqZ1la-N-k_W0eJyhZgpvXfGWSQysEhi7okGPpst9bYUScGjiN9-mfGRGYO3lDN7mrXeXYDGeipdTQrsGDBkhUlYWnCWg6xNxqfKVcw8q9SF1IewAV6RTYfOVvidsUDlYYpNht40QQr8T2lpUA6TvoKcasyQX1kMOZp-knHwutzEy0p67Fkz7hRW2Jrxw", "members/static/members/img/stitch/signup.png"),
    ("https://lh3.googleusercontent.com/aida/ADBb0uh4PU2py-ZU15tWWPiWWUJQJpdwkfAB0D3IPRcPdnUvyEAc4GAT9NH4hFV8MdTD-0wqBxkcDQ1z7RN_zAGx8k6cenbxIWZ4zCfsEoVXjtod1SsjNuaBjx6f4iHziFKhsZvrNrXQr1vy6oop1Emg4clQaE2VGFHowwRK_UXHRDSduL8RPvGYZlSUm2xx6VhfxGAiwM1cmHS-PDC4SG9I0VYSzlSvdCX336jHgWTrwY33omutPCY9gxwneJ0", "members/static/members/img/stitch/home_page.png"),
    ("https://lh3.googleusercontent.com/aida/ADBb0ujMS9LMlEw6G9-YV21lt2UTvNtuBh22sn3Ub3vdlS5ynQDinDax2gvUhlAxIkOYwamL8BQyfBh3V-CWxW6RcxTEwFqVvyF2Ap6EDT6wFmad29NDH4fxyzhojx7oP30-hV9FpGs3S-GuAQ0B39Ns7slTlhkvgKKF55YBSjKU2vfijmqC2h-SCQqhaqCTp4O7q34M75ncL6riq2wVl8sbZrXYoHWdPisNjPyTWGMxNAgfyjvpD83hnW45CQw", "members/static/members/img/stitch/login.png"),
    ("https://lh3.googleusercontent.com/aida/ADBb0ui3qlXIhutjFfrWH6C8F5bfMPWNnabhsy09KLsx9iu4shk-IhacSZQgMxzjGKntgaJyPLCuCLQ6sCZQrYH-mORB51bKY9SA40eydt7oId4500qzJebUT2uW7bkX7dtVw0qmaqZvl_o_ClYQ-b4Z9BzgRmk7hHUUYTaDEfUbmMqREDcVyPkO_WYx1Y5qngBg3CPEohxmT5QkFCnUN36ZazfOeE0IDD7saCPD6vHARFyHVnrPVlgBCIqSHDQ", "members/static/members/img/stitch/dashboard.png"),
    ("https://lh3.googleusercontent.com/aida/ADBb0uiKhMN27_36NJG5HCQcRcDYc5rnlTivpEggixkpwrTU6f8c2aMZv94GytLwqp78-xaXKs3fy7JOF4xaPujOa5u4plm9nwZ191I_uXNKbc4C9QQ9kQ0I1LMOTqdqxx6hUiyP0B8aX3-YcZrJmv-4fuBYOZ6RIb5MtElm6u-3vOQBSDny3eNCheb6XvL_d6H-zxtWC4cyJls8SGjeWMgeylXUyBr_m0MblkkX4dE7mP-l6aFAxeWhArQ5WkQ", "members/static/members/img/stitch/jobs.png"),
    ("https://lh3.googleusercontent.com/aida/ADBb0ujV88zf62s7Iyu_7w9Vk-CQUM5aeHh1VA1jzNgt1G5B8m6t5tsKwxaV5oT3BfWUP1Trb0z86krqQu4_w0wk44BYJgl5JKnKMpFoJCRLWSKsm_wM1A19T0nQMBb3M4NgDlcAaq8cgUMYjK-ZOFOFD5H53tgO68w9SV4UwCl0BsgjTwvhAz3iH6RBZYymVL1mMoZUhq1eAgw2Aa97rS3wxNMDfotf3TL7_LMHQyggqR6kaGfuI9hwR3e8acI", "members/static/members/img/stitch/messages.png"),
]

for url, path in assets:
    download(url, path)
