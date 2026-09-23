"""Modul perbaikan kode untuk melewati Pylint quality gate."""

NILAI_X = 10

def fungsi_yang_benar(nilai_a, nilai_b, nilai_c):
    """Fungsi contoh untuk mendemonstrasikan gaya penulisan PEP 8.

    Args:
        nilai_a: Parameter pertama.
        nilai_b: Parameter kedua.
        nilai_c: Parameter ketiga.

    Returns:
        Nilai kalkulasi jika kondisi terpenuhi, atau None.
    """
    global NILAI_X
    if nilai_a is True and nilai_b is False and nilai_c is None:
        hasil = NILAI_X + 1
        print(f"Hasil: {hasil}")
        return hasil
    return None

def main():
    """Fungsi utama program."""
    fungsi_yang_benar(True, False, None)

if __name__ == "__main__":
    main()