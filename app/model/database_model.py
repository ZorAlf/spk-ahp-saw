from sqlmodel import Field, SQLModel, Relationship

class Opsi_Kriteria(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    id_kriteria: int = Field(foreign_key="kriteria.id", ondelete="CASCADE")
    opsi: str
    bobot: float

    kriteria: "Kriteria" = Relationship(back_populates="opsi_kriteria")
    skor_karyawan: list["Skor_Karyawan"] = Relationship(back_populates="opsi_kriteria", cascade_delete=True)

class Skor_Karyawan(SQLModel, table=True):
    id_karyawan: int = Field(default=None, foreign_key="karyawan.id", primary_key=True, ondelete="CASCADE")
    id_kriteria: int = Field(default=None, foreign_key="kriteria.id", primary_key=True, ondelete="CASCADE")
    id_opsi: int = Field(foreign_key="opsi_kriteria.id", ondelete="CASCADE")

    karyawan: "Karyawan" = Relationship(back_populates="skor_karyawan")
    kriteria: "Kriteria" = Relationship(back_populates="skor_karyawan")
    opsi_kriteria: Opsi_Kriteria = Relationship(back_populates="skor_karyawan")

class Kriteria(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nama: str

    perbandingan_kriteria_1: list["Perbandingan_Kriteria"] = Relationship(
        back_populates="kriteria_1", sa_relationship_kwargs={"foreign_keys": "[Perbandingan_Kriteria.id_kriteria1]"}
    )
    perbandingan_kriteria_2: list["Perbandingan_Kriteria"] = Relationship(
        back_populates="kriteria_2", sa_relationship_kwargs={"foreign_keys": "[Perbandingan_Kriteria.id_kriteria2]"}
    )
    opsi_kriteria: list["Opsi_Kriteria"] = Relationship(back_populates="kriteria", cascade_delete=True)
    skor_karyawan: list["Skor_Karyawan"] = Relationship(back_populates="kriteria", cascade_delete=True)

class Perbandingan_Kriteria(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    id_kriteria1: int = Field(foreign_key="kriteria.id", ondelete="CASCADE")
    nilai_kriteria1: int
    id_kriteria2: int = Field(foreign_key="kriteria.id", ondelete="CASCADE")
    nilai_kriteria2: int

    kriteria_1: Kriteria = Relationship(
        back_populates="perbandingan_kriteria_1", sa_relationship_kwargs={"foreign_keys": "[Perbandingan_Kriteria.id_kriteria1]"}
    )
    kriteria_2: Kriteria = Relationship(
        back_populates="perbandingan_kriteria_2", sa_relationship_kwargs={"foreign_keys": "[Perbandingan_Kriteria.id_kriteria2]"}
    )

class Karyawan(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nama: str

    skor_karyawan: list[Skor_Karyawan] = Relationship(back_populates="karyawan", cascade_delete=True)
