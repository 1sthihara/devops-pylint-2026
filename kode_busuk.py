"""Modul untuk mendemonstrasikan perbaikan kode."""

def tambah_angka(angka_a, angka_b):
    """Fungsi untuk menjumlahkan dua angka.

    Args:
        angka_a: Angka pertama.
        angka_b: Angka kedua.

    Returns:
        Hasil penjumlahan angka_a dan angka_b.
    """
    hasil = angka_a + angka_b
    print(hasil)
    return hasil

if __name__ == "__main__":
    tambah_angka(1, 2)