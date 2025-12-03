import streamlit as st
from datetime import datetime

# ============================================================
# PROGRAM ACCESS CARD - MINING SITE PT INDAH IMUT DAN MERONA
# Versi Streamlit (Web App)
# ============================================================

def init_state():
    if "kelompok" not in st.session_state:
        st.session_state.kelompok = [
            "Damar Restu Wicaksono",
            "Edghar Hazzel Raudhadipta",
            "Tyo Fazira Mukhtar",
            "Shane David Febrian Panjaitan",
            "Fakhira Selima Budiana",
        ]

    if "Nim" not in st.session_state:
        st.session_state.Nim = [
            "16425220",
            "16425300",
            "16425450",
            "16425030",
            "16425100",
        ]

    if "nip" not in st.session_state:
        st.session_state.nip = ["1001", "1002", "1003", "1004", "1005"]

    if "nama" not in st.session_state:
        st.session_state.nama = [
            "Edghar Hazzel",
            "Damar Restu",
            "Shane David",
            "Tyo Fazira",
            "Fakhira",
        ]

    if "jabatan" not in st.session_state:
        st.session_state.jabatan = [
            "Site Manager",
            "Engineer",
            "Safety Officer",
            "Operator",
            "Finance Manager",
        ]

    if "diizinkan" not in st.session_state:
        st.session_state.diizinkan = [
            "Site Manager",
            "Mine Manager",
            "Mine Engineer",
            "Safety Officer",
            "Supervisor",
        ]


def jam_operasional_ditutup() -> bool:
    jam = datetime.now().hour
    return jam >= 18 or jam <= 5


def main():
    init_state()

    # Menampilkan waktu berjalan (tanpa autorefresh library)
    sekarang = datetime.now()
    waktu = sekarang.hour
    menit = sekarang.minute
    detik = sekarang.second

    st.set_page_config(page_title="Access Card - Mining Site", layout="centered")

    # Tombol manual refresh (pengganti st_autorefresh)
    if st.sidebar.button("Refresh Waktu"):
        st.rerun()

    # ============================================
    # HALAMAN UTAMA
    # ============================================
   
    st.title("TamengTambang - Access Card")
    st.subheader("PT INDAH IMUT DAN MERONA")
    st.caption("Jam operasional: 05.00 - 18.00 WIB")
    st.caption(f"{waktu:02d}:{menit:02d} WIB")

    # ============================
    # MENU BARU
    # ============================
    with st.sidebar:
        st.header("Menu")
        menu = st.radio(
            "Pilih menu:",
            (
                "1. Cek Akses Karyawan",
                "2. Ubah Jabatan Karyawan",
                "3. Tambah Karyawan Baru",
                "4. Menambahkan Daftar Akses",
                "5. Lihat Daftar Karyawan",
                "6. Lihat Jabatan yang Diizinkan",
                "7. About Program",
                "8. Keluar dari Program",
            ),
        )

    # ======================================
    # 1. Cek Akses Karyawan
    # ======================================
    if menu.startswith("1"):
        st.header("Cek Akses Karyawan")

        no = st.text_input("Masukkan Nomor Induk Karyawan (NIP)")

        if st.button("Cek Akses"):
            st.session_state.hasil_cek = no

        if "hasil_cek" in st.session_state:
            no = st.session_state.hasil_cek
            ditemukan = False
            nip_list = st.session_state.nip
            nama_list = st.session_state.nama
            jabatan_list = st.session_state.jabatan
            diizinkan = st.session_state.diizinkan

            for i in range(len(nip_list)):
                if no == nip_list[i]:
                    ditemukan = True
                    st.write(f"**Nama:** {nama_list[i]}")
                    st.write(f"**Jabatan:** {jabatan_list[i]}")

                    if jabatan_list[i] in diizinkan:
                        if not jam_operasional_ditutup():
                            st.success(
                                f"Akses DITERIMA. Masuk pada {waktu:02d}:{menit:02d} WIB."
                            )
                        else:
                            st.error("Akses DITOLAK. Melewati JAM OPERASIONAL.")
                    else:
                        st.error("Akses DITOLAK. Jabatan tidak memiliki hak akses.")
                    break

            if not ditemukan:
                st.warning("Nomor Induk Karyawan tidak ditemukan.")

        st.markdown("---")
        st.caption("© PT Indah Imut dan Merona 2025 (Kelompok 1)")

    # ======================================
    # 2. Ubah Jabatan
    # ======================================
    elif menu.startswith("2"):
        st.header("Ubah Jabatan Karyawan")

        nip_edit = st.text_input("Masukkan NIP Karyawan yang Ingin Diubah")
        jabatan_baru = st.text_input("Masukkan Jabatan Baru")

        if st.button("Ubah Jabatan"):
            nip_list = st.session_state.nip
            jabatan_list = st.session_state.jabatan

            if nip_edit in nip_list:
                index = nip_list.index(nip_edit)
                jabatan_list[index] = jabatan_baru
                st.success(
                    f"Jabatan untuk NIP {nip_edit} berhasil diubah menjadi: {jabatan_baru}"
                )
            else:
                st.error("NIP tidak ditemukan!")

        st.markdown("---")
        st.caption("© PT Indah Imut dan Merona 2025 (Kelompok 1)")

    # ======================================
    # 3. Tambah Karyawan
    # ======================================
    elif menu.startswith("3"):
        st.header("Tambah Karyawan Baru")
        nip_baru = st.text_input("Masukkan NIP Baru")
        nama_baru = st.text_input("Masukkan Nama")
        jabatan_baru = st.text_input("Masukkan Jabatan")

        if st.button("Simpan Karyawan Baru"):
            nip_list = st.session_state.nip

            if nip_baru in nip_list:
                st.error("Nomor Induk Karyawan sudah terdaftar!")
            elif not nip_baru or not nama_baru or not jabatan_baru:
                st.warning("Harap lengkapi semua data.")
            else:
                st.session_state.nip.append(nip_baru)
                st.session_state.nama.append(nama_baru)
                st.session_state.jabatan.append(jabatan_baru)
                st.success("Karyawan baru berhasil ditambahkan.")

        st.markdown("---")
        st.caption("© PT Indah Imut dan Merona 2025 (Kelompok 1)")

    # ======================================
    # 4. Tambah Daftar Akses
    # ======================================
    elif menu.startswith("4"):
        st.header("Menambahkan Daftar Akses Jabatan")
        izin_baru = st.text_input("Masukkan Jabatan Baru yang Diizinkan")

        if st.button("Tambah Jabatan Akses"):
            diizinkan = st.session_state.diizinkan

            if izin_baru in diizinkan:
                st.error("Jabatan telah terdaftar!")
            elif not izin_baru:
                st.warning("Harap isi nama jabatan.")
            else:
                diizinkan.append(izin_baru)
                st.success("Jabatan berhasil didaftarkan.")

        st.markdown("---")
        st.caption("© PT Indah Imut dan Merona 2025")

    # ======================================
    # 5. Lihat Daftar Karyawan
    # ======================================
    elif menu.startswith("5"):
        st.header("Daftar Karyawan")

        if st.session_state.nip:
            import pandas as pd

            df = pd.DataFrame(
                {
                    "NIP": st.session_state.nip,
                    "Nama": st.session_state.nama,
                    "Jabatan": st.session_state.jabatan,
                }
            )
            df.index += 1
            df.index.name = "No"

            st.dataframe(df, use_container_width=True)
        else:
            st.info("Belum ada data karyawan.")

        st.markdown("---")
        st.caption("© PT Indah Imut dan Merona 2025")

    # ======================================
    # 6. Lihat Jabatan Akses
    # ======================================
    elif menu.startswith("6"):
        st.header("Jabatan yang Diizinkan Masuk Area Khusus")

        if st.session_state.diizinkan:
            for i, j in enumerate(st.session_state.diizinkan, start=1):
                st.write(f"{i}. {j}")
        else:
            st.info("Belum ada jabatan yang diizinkan.")

        st.markdown("---")
        st.caption("© PT Indah Imut dan Merona 2025")

    # ======================================
    # 7. About Program
    # ======================================
    elif menu.startswith("7"):
        st.header("About Program")

        Nim = st.session_state.Nim
        kelompok = st.session_state.kelompok

        st.write("**NIM - Nama Anggota**")
        for i in range(len(Nim)):
            st.write(f"{Nim[i]} — {kelompok[i]}")

        st.markdown("---")
        st.caption("© PT Indah Imut dan Merona 2025")

    # ======================================
    # 8. Exit
    # ======================================
    elif menu.startswith("8"):
        st.header("Keluar dari Program")
        st.info("Tutup tab untuk keluar aplikasi.")


if __name__ == "__main__":
    main()
