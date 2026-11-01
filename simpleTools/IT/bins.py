def to_bin(*args: int) -> list[str]:
    """
    Переводит любое количество десятичных чисел в бинарную форму
    Args: 
      *args (int): десятичные числа
    Returns: 
      list[str]: список бинарных чисел
    """
    return [str(bin(x)).replace("0b", "") for x in args]
    
def to_oct(*args: int) -> list[str]:
    """
    Переводит любое количество десятичных чисел в восьмиричную форму
    Args: 
      *args (int): десятичные числа
    Returns: 
      list[str]: список восьмиричных чисел
    """
    return [str(oct(x)).replace("0o", "") for x in args]

def to_hex(*args: int) -> list[str]:
    """
    Переводит любое количество десятичных чисел в шестнадцатиричную форму
    Args: 
      *args (int): десятичные числа
    Returns: 
      list[str]: список шестнадцатиричных чисел
    """
    return [str(hex(x)).replace("0x", "") for x in args]
    
def ip_to_bin(address: str) -> str:
    """
    Переводит IP-адрес в бинарный формат
    Args: 
      address (str): IP-адрес
    Returns: 
      str: IP-пдрес в двоичном формате
    Raises: 
      ValueError: Каждый октет передаваемого IP должен быть в диапазоне от 0 до 255
    """
    numbers = address.split(".")
    octets = [int(x) for x in numbers]
    
    for octet in octets:
        if octet >= 256 or octet < 0:
            raise ValueError("Uncorrect IP. Correct numbers are 0-255")
    bin_octets = [str(bin(x)).replace("0b", "") for x in octets]
    
    for octet in bin_octets:
        length = len(octet)
        if length < 8:
            i = bin_octets.index(octet)
            bin_octets[i] = "0" * (8 - length) + octet
    
    final_str = str(bin_octets[0])
    for byte in bin_octets[1:-1]:
        final_str = final_str + "." + str(byte)
    final_str = final_str + "." + bin_octets[-1]
    
    return final_str
        