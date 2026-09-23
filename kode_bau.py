"""Modul perbaikan kode bau agar lolos Pylint."""


def sapa_dunia():
    """Fungsi sederhana untuk menyapa dunia.

    Returns:
        String berisi pesan sapaan.
    """
    pesan = "Halo, Pylint!"
    print(pesan)
    return pesan


if __name__ == "__main__":
    sapa_dunia()
