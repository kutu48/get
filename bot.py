import requests
import random
import time

# Baca daftar proxy dari file
def get_proxies(file_path):
    with open(file_path, 'r') as file:
        proxies = [line.strip() for line in file if line.strip()]
    return proxies

# Baca daftar alamat dari file
def get_addresses(file_path):
    with open(file_path, 'r') as file:
        addresses = [line.strip() for line in file if line.strip()]
    return addresses

# Pilih proxy secara acak dari daftar
def get_random_proxy(proxies):
    return random.choice(proxies)

# Pilih alamat secara acak dari daftar
def get_random_address(addresses):
    return random.choice(addresses)

# Kirim permintaan POST ke API
def send_request(proxy, address):
    url = "https://faucet.vana.org/api/transactions"
    headers = {
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "text/plain;charset=UTF-8",
        "Origin": "https://faucet.vana.org",
        "Referer": "https://faucet.vana.org/",
        "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
    }
    payload = {
        "address": address,
        "captcha": "P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQTuZDsphNUGcYT4vOg7LdJq2HajhM0EI-Wc963yGhBC7EZijljV96rBwlMZtGOIbn5wcf_uar14xbdXypt67d_H75pIsnkoQjU7YSOHMeU_xyQa4VqgnOhnLlBo1JC-f8r_MpBJ09lZo5-MSKtDjYxadHImPqTWVWD300Rv_X6kWADT0hMTHRRsJJf5KU8oAOpEJ6Q43IOl9KkzqL1pDrIktLRQJEIQgHkLgR1PX6CXCiySQC4aPExNHWxzeLsPgMtMqz9X2l9J-j5qbvAOaxZft474JYI_J6FeWeyYdyt68E5JD5Y8I1MgHGT0qECQy8T5Y0mJDLS-2mGPQxPKUbarkJkz2SBnhAn9sN509-XgS8Lk3RCaGk5Ovb_B52oE9M8JBkYkkwpH4YrHkGrlj0cmnCra9E-eFMr4bPXr098xWSHo9wnV-fWRj7N4b9iX9M5dNJyzBCc0tN-_lgdBLlxW5nDpjDqWOkkejgGXbOzzCHsbcWosgxOtEQ-ASggu4rxQhAP_td5gGpkg8I4WF1_r7SR_jsMwrByeV-CQAy7uTVHSFTYKOzHh-lu32xSDeCaZQvZAXXPiY0A2se-3ygTO2dhz43F46U6AA477YH2Kvob96qLLRJlAoLi6HQ15fgK3EXSrqosajTLj2RBEMdaLKGKMgeZQHlUeRQO_RWXNepJwICPPASmD1wIIqkBU_fE12QCyZ-cSfuiPYGt2Jdymsk2i8TYiG4GijIpXUZee85mJbJk7iMj-C2CiGjq3OpzeVOkLLa9qMipYJPH9V_ywhokm_UAJwlyItp8EUh7RDXlFsM_X3iQvsq9bC35F7LHCW2PQKyPl5koX9fpF5Vd787OOhOU4rG8z8WR2JumkAihCiyHorZWv5UGuI5DtSkTGOE_kklZa925evMRgkNn00yL4m7m8RUplOPmzBhLQVUrYFkakgaISYb78fHv_0ObbSfZFQQBu8BT7RfDXKpULf8SLNlc3wde8trdyQlHtJY9TIZG_jKObcB5ogf45xQMsKxGS7mCX3hChmxdvxxeUcSndtehVeO49dr30l2xZ48cVmF5jdSXFmowkPqRmPKpx6nrbfrLcwMOO5vM3PIkJ1To9KjvAVTL-Xgavll0Jy0xLMMVR4UzAcQztKeyhj8vgpvRCPf9so4bNkn_xq0v5Fnqu1TCxAMfZuLpBEUoisDzRGrfrQ4K1Q2dW0ItNmiPX4kiPpj1LsbGjtMhn7f93tQbD1i6INzNv-Bzprx_ZvsVyDn899kFQZfl80sGI1_3-rsAgzL5v0iLMvtYFLVn9VQbFgdkaDaaXnAoqCIFGRsdGgt9Kmc_brRwkD8Iy9uKb5C_g0L-duoUnX36_KoK1gq0nzyGYN24bPRKeyppr2RjIYe1Lu4z8d_8Lo1vje3pyBFuc-YM9gSeVkE2emPZBoeAhW7mdpT54qnJbO5363TwG-O_auXDEiq8I6-uJElz3RmB6vlebD89UWHb3MJq1Lqjk6h3FdYEOb2abXuUs6Le7Sz0MBGhikn0GWymjHcQ7GjT1D4Sg84mzulbmsoZRVkdmjzMOknL3V3F_ifFNc1IbodtAdV9kd-ZvgvPFKjfRDOnOqVb73bxZK0WDjBvll5iWtP1Bicr3ZhcLTMn6x8yADsfCqkL1bPtUAutZEdQGaYuiEHkAaRdr9xhL4F2jZXhwzmap1Geoc2hhcmRfaWTOD3Lqb6JrcqdmMjlkNzJhonBkAA.NbS3LFsFShx--bsLbPEcmZ-Rv2_e1deASbFVFdipCkY"
    }

    try:
        response = requests.post(
            url, json=payload, headers=headers, proxies={"http": proxy, "https": proxy}
        )
        print(response.json())
    except Exception as e:
        print(f"Error using proxy {proxy}: {e}")

def main():
    proxies = get_proxies("proxy.txt")
    addresses = get_addresses("address.txt")
    if not proxies:
        print("No proxies found.")
        return
    if not addresses:
        print("No addresses found.")
        return

    while True:
        proxy = get_random_proxy(proxies)
        address = get_random_address(addresses)
        print(f"Using proxy: {proxy}, address: {address}")
        send_request(proxy, address)
        time.sleep(3600)  # Menunggu selama satu jam sebelum melakukan permintaan berikutnya

if __name__ == "__main__":
    main()
