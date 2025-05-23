USE [master]
GO
/****** Object:  Database [StudentManager]    Script Date: 10/10/2024 6:7:8 PM ******/
CREATE DATABASE [StudentManager]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'StudentManager', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\DATA\StudentManager.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'StudentManager_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\DATA\StudentManager_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
GO
ALTER DATABASE [StudentManager] SET COMPATIBILITY_LEVEL = 140
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [StudentManager].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [StudentManager] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [StudentManager] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [StudentManager] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [StudentManager] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [StudentManager] SET ARITHABORT OFF 
GO
ALTER DATABASE [StudentManager] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [StudentManager] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [StudentManager] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [StudentManager] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [StudentManager] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [StudentManager] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [StudentManager] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [StudentManager] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [StudentManager] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [StudentManager] SET  DISABLE_BROKER 
GO
ALTER DATABASE [StudentManager] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [StudentManager] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [StudentManager] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [StudentManager] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [StudentManager] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [StudentManager] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [StudentManager] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [StudentManager] SET RECOVERY FULL 
GO
ALTER DATABASE [StudentManager] SET  MULTI_USER 
GO
ALTER DATABASE [StudentManager] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [StudentManager] SET DB_CHAINING OFF 
GO
ALTER DATABASE [StudentManager] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [StudentManager] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [StudentManager] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [StudentManager] SET QUERY_STORE = OFF
GO
USE [StudentManager]
GO
ALTER DATABASE SCOPED CONFIGURATION SET IDENTITY_CACHE = ON;
GO
ALTER DATABASE SCOPED CONFIGURATION SET LEGACY_CARDINALITY_ESTIMATION = OFF;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET LEGACY_CARDINALITY_ESTIMATION = PRIMARY;
GO
ALTER DATABASE SCOPED CONFIGURATION SET MAXDOP = 0;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET MAXDOP = PRIMARY;
GO
ALTER DATABASE SCOPED CONFIGURATION SET PARAMETER_SNIFFING = ON;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET PARAMETER_SNIFFING = PRIMARY;
GO
ALTER DATABASE SCOPED CONFIGURATION SET QUERY_OPTIMIZER_HOTFIXES = OFF;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET QUERY_OPTIMIZER_HOTFIXES = PRIMARY;
GO
USE [StudentManager]
GO
/****** Object:  Table [dbo].[SinhVien]    Script Date: 10/10/2024 6:7:8 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SinhVien](
	[mssv] [varchar](50) NOT NULL,
	[ho] [nvarchar](50) NOT NULL,
	[dem] [nvarchar](50) NULL,
	[ten] [nvarchar](50) NOT NULL,
	[ngay_sinh] [datetime] NOT NULL,
	[ma_lop] [varchar](20) NOT NULL,
	[email] [nvarchar](255) NULL,
	[so_dt] [varchar](50) NULL,
	[dia_chi] [nvarchar](255) NULL,
	[he_hoc] [nvarchar](50) NULL,
	[trang_thai] [nvarchar](50) NULL,
	[image] [image] NULL,
	[ma_ctdt] [int] NOT NULL,
 CONSTRAINT [PK_SinhVien] PRIMARY KEY CLUSTERED 
(
	[mssv] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[LopSV]    Script Date: 10/10/2024 6:7:9 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[LopSV](
	[ma_lop] [varchar](20) NOT NULL,
	[ten_lop] [nvarchar](50) NOT NULL,
	[ma_khoa] [varchar](20) NOT NULL,
 CONSTRAINT [PK_LopSV] PRIMARY KEY CLUSTERED 
(
	[ma_lop] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[ThongTinSV]    Script Date: 10/10/2024 6:7:9 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[ThongTinSV]
AS
SELECT        dbo.SinhVien.mssv, dbo.SinhVien.ngay_sinh, dbo.SinhVien.ma_lop, dbo.SinhVien.email, dbo.SinhVien.so_dt, dbo.SinhVien.dia_chi, dbo.SinhVien.he_hoc, dbo.SinhVien.trang_thai, dbo.LopSV.ten_lop, CONCAT_WS(' ', 
                         dbo.SinhVien.ho, dbo.SinhVien.dem, dbo.SinhVien.ten) AS ho_ten, dbo.SinhVien.image
FROM            dbo.LopSV INNER JOIN
                         dbo.SinhVien ON dbo.LopSV.ma_lop = dbo.SinhVien.ma_lop
GO
/****** Object:  View [dbo].[DsLopSV]    Script Date: 10/10/2024 6:7:9 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[DsLopSV]
AS
SELECT        dbo.SinhVien.mssv, dbo.SinhVien.ho, dbo.SinhVien.dem, dbo.SinhVien.ten, dbo.SinhVien.ngay_sinh, dbo.LopSV.ten_lop
FROM            dbo.LopSV INNER JOIN
                         dbo.SinhVien ON dbo.LopSV.ma_lop = dbo.SinhVien.ma_lop
GO
/****** Object:  Table [dbo].[HocPhan]    Script Date: 10/10/2024 6:7:9 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[HocPhan](
	[ma_hp] [varchar](20) NOT NULL,
	[ten_hp] [nvarchar](255) NOT NULL,
	[thoi_luong] [varchar](12) NOT NULL,
	[tinchi] [tinyint] NOT NULL,
	[tinchi_hocphi] [float] NOT NULL,
	[trong_so] [float] NOT NULL,
	[ma_khoa] [varchar](20) NULL,
 CONSTRAINT [PK_HocPhan] PRIMARY KEY CLUSTERED 
(
	[ma_hp] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[DangKyLop]    Script Date: 10/10/2024 6:7:9 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[DangKyLop](
	[mssv] [varchar](50) NOT NULL,
	[ma_lop_dk] [int] NOT NULL,
	[hoc_ky] [varchar](8) NOT NULL,
	[diem_qt] [float] NULL,
	[diem_ck] [float] NULL,
	[diem_chu] [varchar](2) NULL,
 CONSTRAINT [PK_DangKyLop_1] PRIMARY KEY CLUSTERED 
(
	[mssv] ASC,
	[ma_lop_dk] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[LopDK]    Script Date: 10/10/2024 6:7:9 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[LopDK](
	[ma_hp] [varchar](20) NOT NULL,
	[sl_dk] [smallint] NULL,
	[sl_toida] [smallint] NULL,
	[loai_lop] [varchar](50) NULL,
	[trang_thai] [nvarchar](50) NULL,
	[ma_lop_dk] [int] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_LopDK] PRIMARY KEY CLUSTERED 
(
	[ma_lop_dk] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[BangdiemSV]    Script Date: 10/10/2024 6:7:9 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[BangdiemSV]
AS
SELECT        dbo.DangKyLop.mssv, dbo.DangKyLop.ma_lop_dk, dbo.DangKyLop.hoc_ky, dbo.DangKyLop.diem_qt, dbo.DangKyLop.diem_ck, dbo.DangKyLop.diem_chu, dbo.HocPhan.ten_hp, dbo.HocPhan.ma_hp, dbo.HocPhan.tinchi
FROM            dbo.DangKyLop INNER JOIN
                         dbo.LopDK ON dbo.DangKyLop.ma_lop_dk = dbo.LopDK.ma_lop_dk INNER JOIN
                         dbo.HocPhan ON dbo.LopDK.ma_hp = dbo.HocPhan.ma_hp
WHERE        (dbo.DangKyLop.diem_chu IS NOT NULL)
GO
/****** Object:  Table [dbo].[KhoaVien]    Script Date: 10/10/2024 6:7:9 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[KhoaVien](
	[ma_khoa] [varchar](20) NOT NULL,
	[ten_khoa] [nvarchar](255) NOT NULL,
 CONSTRAINT [PK_KhoaVien_1] PRIMARY KEY CLUSTERED 
(
	[ma_khoa] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[DsHP]    Script Date: 10/10/2024 6:7:9 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[DsHP]
AS
SELECT        dbo.HocPhan.ma_hp, dbo.HocPhan.ten_hp, dbo.HocPhan.thoi_luong, dbo.HocPhan.tinchi, dbo.HocPhan.tinchi_hocphi, dbo.HocPhan.trong_so, dbo.KhoaVien.ten_khoa
FROM            dbo.HocPhan INNER JOIN
                         dbo.KhoaVien ON dbo.HocPhan.ma_khoa = dbo.KhoaVien.ma_khoa
GO
/****** Object:  Table [dbo].[ChuongTrinhDT]    Script Date: 10/10/2024 6:7:9 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ChuongTrinhDT](
	[ma_ctdt] [int] NOT NULL,
	[ten_ctdt] [nvarchar](255) NOT NULL,
 CONSTRAINT [PK_ChuongTrinhDT] PRIMARY KEY CLUSTERED 
(
	[ma_ctdt] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[DangKyHP]    Script Date: 10/10/2024 6:7:9 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[DangKyHP](
	[mssv] [varchar](50) NOT NULL,
	[ma_hp] [varchar](20) NOT NULL,
	[hoc_ky] [varchar](8) NOT NULL,
	[ngay_dk] [date] NOT NULL,
 CONSTRAINT [PK_DangKyHP] PRIMARY KEY CLUSTERED 
(
	[mssv] ASC,
	[ma_hp] ASC,
	[hoc_ky] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[HocKyMoDK]    Script Date: 10/10/2024 6:7:9 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[HocKyMoDK](
	[hoc_ky] [varchar](8) NOT NULL,
 CONSTRAINT [PK_HocKyMoDK] PRIMARY KEY CLUSTERED 
(
	[hoc_ky] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[HocPhanCTDT]    Script Date: 10/10/2024 6:7:9 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[HocPhanCTDT](
	[ma_ctdt] [int] NOT NULL,
	[ma_hp] [varchar](20) NOT NULL,
 CONSTRAINT [PK_HocPhanCTDT] PRIMARY KEY CLUSTERED 
(
	[ma_ctdt] ASC,
	[ma_hp] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[KetQuaHT]    Script Date: 10/10/2024 6:7:9 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[KetQuaHT](
	[hoc_ky] [varchar](8) NOT NULL,
	[mssv] [varchar](50) NOT NULL,
	[gpa] [float] NOT NULL,
	[cpa] [float] NOT NULL,
 CONSTRAINT [PK_GPA] PRIMARY KEY CLUSTERED 
(
	[hoc_ky] ASC,
	[mssv] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PhanQuyenLopDK]    Script Date: 10/10/2024 6:7:10 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PhanQuyenLopDK](
	[ma_lop_dk] [int] NOT NULL,
	[ma_giaovien] [varchar](50) NOT NULL,
 CONSTRAINT [PK_PhanQuyenLopDK] PRIMARY KEY CLUSTERED 
(
	[ma_lop_dk] ASC,
	[ma_giaovien] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[RangBuocHP]    Script Date: 10/10/2024 6:7:10 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[RangBuocHP](
	[ma_hp] [varchar](20) NOT NULL,
	[ma_hpdk] [varchar](20) NOT NULL,
	[loai_dk] [varchar](50) NULL,
 CONSTRAINT [PK_RangBuocHP] PRIMARY KEY CLUSTERED 
(
	[ma_hp] ASC,
	[ma_hpdk] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Users]    Script Date: 10/10/2024 6:7:10 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Users](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[user_name] [varchar](50) NOT NULL,
	[pass_word] [varchar](255) NOT NULL,
	[permission] [varchar](2) NOT NULL,
 CONSTRAINT [PK_Users] PRIMARY KEY CLUSTERED 
(
	[user_name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[KetQuaHT] ADD  CONSTRAINT [DF_GPA_gpa]  DEFAULT ((0)) FOR [gpa]
GO
ALTER TABLE [dbo].[KetQuaHT] ADD  CONSTRAINT [DF_KetQuaHT_cpa]  DEFAULT ((0)) FOR [cpa]
GO
ALTER TABLE [dbo].[DangKyHP]  WITH CHECK ADD  CONSTRAINT [FK_DangKyHP_HocKyMoDK] FOREIGN KEY([hoc_ky])
REFERENCES [dbo].[HocKyMoDK] ([hoc_ky])
GO
ALTER TABLE [dbo].[DangKyHP] CHECK CONSTRAINT [FK_DangKyHP_HocKyMoDK]
GO
ALTER TABLE [dbo].[DangKyHP]  WITH CHECK ADD  CONSTRAINT [FK_DangKyHP_HocPhan] FOREIGN KEY([ma_hp])
REFERENCES [dbo].[HocPhan] ([ma_hp])
GO
ALTER TABLE [dbo].[DangKyHP] CHECK CONSTRAINT [FK_DangKyHP_HocPhan]
GO
ALTER TABLE [dbo].[DangKyHP]  WITH CHECK ADD  CONSTRAINT [FK_DangKyHP_SinhVien] FOREIGN KEY([mssv])
REFERENCES [dbo].[SinhVien] ([mssv])
GO
ALTER TABLE [dbo].[DangKyHP] CHECK CONSTRAINT [FK_DangKyHP_SinhVien]
GO
ALTER TABLE [dbo].[DangKyLop]  WITH CHECK ADD  CONSTRAINT [FK_DangKyLop_LopDK] FOREIGN KEY([ma_lop_dk])
REFERENCES [dbo].[LopDK] ([ma_lop_dk])
GO
ALTER TABLE [dbo].[DangKyLop] CHECK CONSTRAINT [FK_DangKyLop_LopDK]
GO
ALTER TABLE [dbo].[DangKyLop]  WITH CHECK ADD  CONSTRAINT [FK_DangKyLop_SinhVien] FOREIGN KEY([mssv])
REFERENCES [dbo].[SinhVien] ([mssv])
GO
ALTER TABLE [dbo].[DangKyLop] CHECK CONSTRAINT [FK_DangKyLop_SinhVien]
GO
ALTER TABLE [dbo].[HocPhan]  WITH CHECK ADD  CONSTRAINT [FK_HocPhan_KhoaVien] FOREIGN KEY([ma_khoa])
REFERENCES [dbo].[KhoaVien] ([ma_khoa])
GO
ALTER TABLE [dbo].[HocPhan] CHECK CONSTRAINT [FK_HocPhan_KhoaVien]
GO
ALTER TABLE [dbo].[HocPhanCTDT]  WITH CHECK ADD  CONSTRAINT [FK_HocPhanCTDT_ChuongTrinhDT] FOREIGN KEY([ma_ctdt])
REFERENCES [dbo].[ChuongTrinhDT] ([ma_ctdt])
GO
ALTER TABLE [dbo].[HocPhanCTDT] CHECK CONSTRAINT [FK_HocPhanCTDT_ChuongTrinhDT]
GO
ALTER TABLE [dbo].[HocPhanCTDT]  WITH CHECK ADD  CONSTRAINT [FK_HocPhanCTDT_HocPhan] FOREIGN KEY([ma_hp])
REFERENCES [dbo].[HocPhan] ([ma_hp])
GO
ALTER TABLE [dbo].[HocPhanCTDT] CHECK CONSTRAINT [FK_HocPhanCTDT_HocPhan]
GO
ALTER TABLE [dbo].[KetQuaHT]  WITH CHECK ADD  CONSTRAINT [FK_GPA_SinhVien] FOREIGN KEY([mssv])
REFERENCES [dbo].[SinhVien] ([mssv])
GO
ALTER TABLE [dbo].[KetQuaHT] CHECK CONSTRAINT [FK_GPA_SinhVien]
GO
ALTER TABLE [dbo].[LopDK]  WITH CHECK ADD  CONSTRAINT [FK_LopDK_HocPhan] FOREIGN KEY([ma_hp])
REFERENCES [dbo].[HocPhan] ([ma_hp])
GO
ALTER TABLE [dbo].[LopDK] CHECK CONSTRAINT [FK_LopDK_HocPhan]
GO
ALTER TABLE [dbo].[LopSV]  WITH CHECK ADD  CONSTRAINT [FK_LopSV_KhoaVien] FOREIGN KEY([ma_khoa])
REFERENCES [dbo].[KhoaVien] ([ma_khoa])
GO
ALTER TABLE [dbo].[LopSV] CHECK CONSTRAINT [FK_LopSV_KhoaVien]
GO
ALTER TABLE [dbo].[PhanQuyenLopDK]  WITH CHECK ADD  CONSTRAINT [FK_PhanQuyenLopDK_LopDK] FOREIGN KEY([ma_lop_dk])
REFERENCES [dbo].[LopDK] ([ma_lop_dk])
GO
ALTER TABLE [dbo].[PhanQuyenLopDK] CHECK CONSTRAINT [FK_PhanQuyenLopDK_LopDK]
GO
ALTER TABLE [dbo].[PhanQuyenLopDK]  WITH CHECK ADD  CONSTRAINT [FK_PhanQuyenLopDK_Users] FOREIGN KEY([ma_giaovien])
REFERENCES [dbo].[Users] ([user_name])
GO
ALTER TABLE [dbo].[PhanQuyenLopDK] CHECK CONSTRAINT [FK_PhanQuyenLopDK_Users]
GO
ALTER TABLE [dbo].[RangBuocHP]  WITH CHECK ADD  CONSTRAINT [FK_RangBuocHP_HocPhan] FOREIGN KEY([ma_hp])
REFERENCES [dbo].[HocPhan] ([ma_hp])
GO
ALTER TABLE [dbo].[RangBuocHP] CHECK CONSTRAINT [FK_RangBuocHP_HocPhan]
GO
ALTER TABLE [dbo].[RangBuocHP]  WITH CHECK ADD  CONSTRAINT [FK_RangBuocHP_HocPhan1] FOREIGN KEY([ma_hpdk])
REFERENCES [dbo].[HocPhan] ([ma_hp])
GO
ALTER TABLE [dbo].[RangBuocHP] CHECK CONSTRAINT [FK_RangBuocHP_HocPhan1]
GO
ALTER TABLE [dbo].[SinhVien]  WITH CHECK ADD  CONSTRAINT [FK_SinhVien_ChuongTrinhDT] FOREIGN KEY([ma_ctdt])
REFERENCES [dbo].[ChuongTrinhDT] ([ma_ctdt])
GO
ALTER TABLE [dbo].[SinhVien] CHECK CONSTRAINT [FK_SinhVien_ChuongTrinhDT]
GO
ALTER TABLE [dbo].[SinhVien]  WITH CHECK ADD  CONSTRAINT [FK_SinhVien_LopSV] FOREIGN KEY([ma_lop])
REFERENCES [dbo].[LopSV] ([ma_lop])
GO
ALTER TABLE [dbo].[SinhVien] CHECK CONSTRAINT [FK_SinhVien_LopSV]
GO
ALTER TABLE [dbo].[SinhVien]  WITH CHECK ADD  CONSTRAINT [FK_SinhVien_Users] FOREIGN KEY([mssv])
REFERENCES [dbo].[Users] ([user_name])
GO
ALTER TABLE [dbo].[SinhVien] CHECK CONSTRAINT [FK_SinhVien_Users]
GO
ALTER TABLE [dbo].[DangKyLop]  WITH CHECK ADD  CONSTRAINT [CK_DangKyLop] CHECK  (([diem_qt]>=(0) AND [diem_qt]<=(10)))
GO
ALTER TABLE [dbo].[DangKyLop] CHECK CONSTRAINT [CK_DangKyLop]
GO
ALTER TABLE [dbo].[DangKyLop]  WITH CHECK ADD  CONSTRAINT [CK_DangKyLop_1] CHECK  (([diem_ck]>=(0) AND [diem_ck]<=(10)))
GO
ALTER TABLE [dbo].[DangKyLop] CHECK CONSTRAINT [CK_DangKyLop_1]
GO
ALTER TABLE [dbo].[DangKyLop]  WITH CHECK ADD  CONSTRAINT [CK_DangKyLop_2] CHECK  (([diem_chu]='R' OR [diem_chu]='I' OR [diem_chu]='F' OR [diem_chu]='D' OR [diem_chu]='D+' OR [diem_chu]='C' OR [diem_chu]='C+' OR [diem_chu]='B' OR [diem_chu]='B+' OR [diem_chu]='A' OR [diem_chu]='A+'))
GO
ALTER TABLE [dbo].[DangKyLop] CHECK CONSTRAINT [CK_DangKyLop_2]
GO
ALTER TABLE [dbo].[RangBuocHP]  WITH CHECK ADD  CONSTRAINT [CK_RangBuocHP] CHECK  (([loai_dk]='t' OR [loai_dk]='h' OR [loai_dk]='s'))
GO
ALTER TABLE [dbo].[RangBuocHP] CHECK CONSTRAINT [CK_RangBuocHP]
GO
ALTER TABLE [dbo].[Users]  WITH CHECK ADD  CONSTRAINT [CK_Users_permission] CHECK  (([permission]='a' OR [permission]='s' OR [permission]='g'))
GO
ALTER TABLE [dbo].[Users] CHECK CONSTRAINT [CK_Users_permission]
GO
ALTER TABLE [dbo].[Users]  WITH CHECK ADD  CONSTRAINT [CK_Users_username] CHECK  (([permission]='s' AND [user_name] like '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]' OR [permission]='a' OR [permission]='g'))
GO
ALTER TABLE [dbo].[Users] CHECK CONSTRAINT [CK_Users_username]
GO
/****** Object:  StoredProcedure [dbo].[changePassWord]    Script Date: 10/10/2024 6:7:10 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[changePassWord]
	@old_pass varchar(255), @new_pass varchar(255), @user_name varchar(50)
AS
BEGIN
	SET NOCOUNT ON;

	DECLARE @retval INT;

	IF (SELECT COUNT(*) FROM Users WHERE Users.user_name = @user_name AND Users.pass_word = @old_pass) > 0
	BEGIN
		UPDATE Users SET pass_word = @new_pass WHERE user_name = @user_name;
		SET @retval = 0;
	END
	ELSE SET @retval = 1;

	SELECT @retval AS RetVal;
END
GO
/****** Object:  StoredProcedure [dbo].[checkDkhp]    Script Date: 10/10/2024 6:7:10 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[checkDkhp]
	@maHp varchar(20), @mssv varchar(50)
AS
BEGIN
	SET NOCOUNT ON;
	DECLARE @retVal nvarchar(255);
	SET @retVal = '';
	
	IF (SELECT COUNT(*)
		FROM(
			(SELECT ma_ctdt FROM SinhVien WHERE @mssv = mssv)t1
			INNER JOIN
			(SELECT ma_ctdt FROM HocPhanCTDT WHERE @maHp = ma_hp)t2
			ON t1.ma_ctdt = t2.ma_ctdt
		)
	) > 0
	BEGIN
		DECLARE @hocTruoc nvarchar(255);
		DECLARE @tienQuyet nvarchar(255);
		DECLARE @songHanh nvarchar(255);

		DECLARE @BangDiemSinhVien table
		(diem_chu varchar(2), ma_hp varchar(20));
	
		INSERT INTO @BangDiemSinhVien(diem_chu, ma_hp) 
		SELECT diem_chu, ma_hp
		FROM dbo.BangdiemSV WHERE mssv=@mssv;

		DECLARE curModuleConstraint CURSOR
		FOR SELECT ma_hpdk, loai_dk FROM dbo.RangBuocHP WHERE ma_hp=@maHp;
		
		DECLARE @maHpDk varchar(20), @loaiDk varchar(50);
		OPEN curModuleConstraint;

		WHILE(0=0)
		BEGIN
			FETCH NEXT FROM curModuleConstraint into @maHpDk, @loaiDk;
			IF(@@FETCH_STATUS <> 0) break;

			IF @loaiDk = 'h'
			BEGIN
				IF((SELECT COUNT(*) FROM @BangDiemSinhVien WHERE ma_hp = @maHpDk) <= 0)
					SET @hocTruoc = CONCAT_WS(', ', @hocTruoc, @maHpDk);
			END
			ElSE IF @loaiDk = 't'
			BEGIN
				IF((SELECT COUNT(*) FROM @BangDiemSinhVien
				WHERE diem_chu IN ('A', 'A+','B', 'B+', 'C', 'C+', 'D', 'D+') AND ma_hp = @maHpDk) <= 0) 
					SET @tienQuyet = CONCAT_WS(', ', @tienQuyet, @maHpDk);
			END
			ELSE IF @loaiDk = 's'
			BEGIN
				;
				IF ((SELECT COUNT(*) FROM @BangDiemSinhVien WHERE ma_hp = @maHpDk) <= 0)
				BEGIN
					IF ((SELECT COUNT(*) FROM DangKyHP WHERE ma_hp = @maHpDk) <= 0) 
						SET @songHanh = CONCAT_WS(', ', @songHanh, @maHpDk);
				END
			END
		END

		CLOSE curModuleConstraint;
		DEALLOCATE curModuleConstraint;

		IF (@tienQuyet <> '') SET @retVal = CONCAT(@retVal, '; ', N'thiếu học phần tiên quyết ', @tienQuyet); 
		IF (@hocTruoc <> '') SET @retVal = CONCAT(@retVal, '; ', N'thiếu học phần học trước ', @hocTruoc); 
		IF (@songHanh <> '') SET @retVal = CONCAT(@retVal, '; ', N'thiếu học phần song hành ', @songHanh); 
	END
	ELSE
	BEGIN
		SET @retVal = CONCAT(@maHp,N' Không nằm trong chương trình đào tạo.');
	END

	SELECT @retVal AS retVal;
END
GO
/****** Object:  StoredProcedure [dbo].[checkLogin]    Script Date: 10/10/2024 6:7:10 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[checkLogin]
	@user_name varchar(50), @pass_word varchar(255)
AS
BEGIN
	SET NOCOUNT ON;
	DECLARE @retVal INT;
	DECLARE @type VARCHAR(2);

	SELECT @type = Users.permission FROM [dbo].[Users] 
	WHERE Users.user_name = @user_name AND Users.pass_word = @pass_word;

    IF (@@ROWCOUNT > 0)
	BEGIN
		SET @retVal = 
		CASE @type
			WHEN 'a' THEN 0
			WHEN 'g' THEN 1
			WHEN 's' THEN 2
		END; --Login success
	END
	ELSE
		SET @retVal = -1; --Access denied

	SELECT @retVal AS RetVal;
END
GO
/****** Object:  StoredProcedure [dbo].[get_countByClass]    Script Date: 10/10/2024 6:7:10 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[get_countByClass]
	@ten_lop nvarchar(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT COUNT(*) FROM DsLopSV WHERE ten_lop = @ten_lop;
END
GO
/****** Object:  StoredProcedure [dbo].[get_countByStudentName]    Script Date: 10/10/2024 6:7:10 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[get_countByStudentName]
	@ho_ten nvarchar(255)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT COUNT(*) FROM DsLopSV WHERE CONCAT_WS(' ', DsLopSV.ho, DsLopSV.dem, DsLopSV.ten) =@ho_ten;
END
GO
/****** Object:  StoredProcedure [dbo].[get_diemForTeacherCc]    Script Date: 10/10/2024 6:7:10 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[get_diemForTeacherCc]
	@classCode int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    SELECT        dbo.DangKyLop.mssv, dbo.DangKyLop.ma_lop_dk, dbo.DangKyLop.hoc_ky, dbo.DangKyLop.diem_qt, dbo.DangKyLop.diem_ck, dbo.DangKyLop.diem_chu, dbo.HocPhan.ten_hp, dbo.HocPhan.ma_hp, dbo.HocPhan.tinchi
	FROM            dbo.DangKyLop INNER JOIN
							 dbo.LopDK ON dbo.DangKyLop.ma_lop_dk = dbo.LopDK.ma_lop_dk INNER JOIN
							 dbo.HocPhan ON dbo.LopDK.ma_hp = dbo.HocPhan.ma_hp
	WHERE dbo.DangKyLop.ma_lop_dk=@classCode;
END
GO
/****** Object:  StoredProcedure [dbo].[get_diemForTeacherSc]    Script Date: 10/10/2024 6:7:10 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[get_diemForTeacherSc]
	@studentCode varchar(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    SELECT        dbo.DangKyLop.mssv, dbo.DangKyLop.ma_lop_dk, dbo.DangKyLop.hoc_ky, dbo.DangKyLop.diem_qt, dbo.DangKyLop.diem_ck, dbo.DangKyLop.diem_chu, dbo.HocPhan.ten_hp, dbo.HocPhan.ma_hp, dbo.HocPhan.tinchi
	FROM            dbo.DangKyLop INNER JOIN
							 dbo.LopDK ON dbo.DangKyLop.ma_lop_dk = dbo.LopDK.ma_lop_dk INNER JOIN
							 dbo.HocPhan ON dbo.LopDK.ma_hp = dbo.HocPhan.ma_hp
	WHERE mssv=@studentCode;
END
GO
/****** Object:  StoredProcedure [dbo].[getDsTenLop]    Script Date: 10/10/2024 6:7:10 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[getDsTenLop]
	@khoa_hoc varchar(255), @ten_khoa nvarchar(255)
AS
BEGIN
	SET NOCOUNT ON;
	SELECT ten_lop 
	FROM LopSV INNER JOIN KhoaVien ON LopSV.ma_khoa = KhoaVien.ma_khoa
	WHERE ten_khoa = @ten_khoa
	AND REVERSE(SUBSTRING(REVERSE(ma_lop), 1, CHARINDEX('K', REVERSE(ma_lop)) - 1)) = @khoa_hoc;
END
GO
/****** Object:  StoredProcedure [dbo].[getKetQuaHocTap]    Script Date: 10/10/2024 6:7:10 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[getKetQuaHocTap]
	@mssv varchar(50)
AS
BEGIN
	SET NOCOUNT ON;
	DECLARE @BangDiemSinhVien table
	(ma_lop_dk int, hoc_ky varchar(8), diem_qt float, diem_ck float, diem_chu varchar(2), ma_hp varchar(20), tinchi int);
	
	INSERT INTO @BangDiemSinhVien(ma_lop_dk, hoc_ky, diem_qt, diem_ck, diem_chu, ma_hp, tinchi) 
	SELECT ma_lop_dk, hoc_ky, diem_qt, diem_ck, diem_chu, ma_hp, tinchi 
	FROM BangdiemSV WHERE mssv=@mssv;
	
	DECLARE @KetQuaHocTap table
	(hoc_ky varchar(8), gpa float, cpa float, tc_qua int, tc_tich_luy int, tc_no_dk int, tc_dk int, thieu_diem varchar(255), trinh_do nvarchar(255));

	INSERT INTO @KetQuaHocTap(hoc_ky, gpa, cpa) SELECT hoc_ky, gpa, cpa FROM KetQuaHT WHERE mssv=@mssv;

	DECLARE curHocKy CURSOR
	FOR SELECT DISTINCT hoc_ky FROM KetQuaHT WHERE mssv=@mssv;

	OPEN curHocKy;
	DECLARE @hocKy varchar(8);
	DECLARE @tinChiTichLuy int;
	DECLARE @tinChiQua int;
	DECLARE @tinChiDK int;
	DECLARE @thieuDiem varchar(255);

	WHILE(0 = 0)
	BEGIN
		SET @thieuDiem = '';
		FETCH NEXT FROM curHocKy into @hocKy;
		IF(@@FETCH_STATUS <> 0) break;

		SELECT @tinChiTichLuy = SUM(tinchi) FROM HocPhan WHERE ma_hp IN 
		(
			SELECT DISTINCT ma_hp FROM @BangDiemSinhVien
			WHERE diem_chu IN ('A', 'A+','B', 'B+', 'C', 'C+', 'D', 'D+') AND hoc_ky <= @hocKy
		);

		UPDATE @KetQuaHocTap SET tc_tich_luy = @tinChiTichLuy WHERE hoc_ky = @hocKy;
		
		SELECT @tinChiDK = SUM(tinchi) FROM HocPhan WHERE ma_hp IN
		(
			SELECT DISTINCT HocPhan.ma_hp
			FROM DangKyLop 
				INNER JOIN LopDK ON DangKyLop.ma_lop_dk = LopDK.ma_lop_dk
				INNER JOIN HocPhan ON LopDK.ma_hp = HocPhan.ma_hp
			WHERE mssv = @mssv AND hoc_ky <= @hocKy
		);

		UPDATE @KetQuaHocTap SET tc_dk = @tinChiDK WHERE hoc_ky = @hocKy;
		UPDATE @KetQuaHocTap SET tc_no_dk = @tinChiDK - @tinChiTichLuy WHERE hoc_ky = @hocKy;

		SELECT @tinChiQua = SUM(tinchi) FROM @BangDiemSinhVien
		WHERE diem_chu IN ('A', 'A+','B', 'B+', 'C', 'C+', 'D', 'D+') AND hoc_ky = @hocKy;

		UPDATE @KetQuaHocTap SET tc_qua = @tinChiQua WHERE hoc_ky = @hocKy;
		SELECT @thieuDiem = CONCAT(@thieuDiem, ma_hp, ';') FROM
		(
			SELECT ma_hp FROM DangKyLop INNER JOIN LopDK ON DangKyLop.ma_lop_dk = LopDK.ma_lop_dk
			WHERE hoc_ky <= @hocKy
			EXCEPT
			SELECT ma_hp FROM @BangDiemSinhVien 
			WHERE hoc_ky <= @hocKy
		) table1;

		UPDATE @KetQuaHocTap SET thieu_diem = @thieuDiem WHERE hoc_ky = @hocKy;

		UPDATE @KetQuaHocTap SET trinh_do = 
		(
			CASE 
				WHEN @tinChiTichLuy < 32 THEN N'Năm thứ nhât'
				WHEN @tinChiTichLuy < 64 THEN N'Năm thứ hai'
				WHEN @tinChiTichLuy < 96 THEN N'Năm thứ ba'
				WHEN @tinChiTichLuy < 128 THEN N'Năm thứ tư'
				ELSE N'Năm thứ năm'
			END
		) WHERE hoc_ky = @hocKy;
	END

	CLOSE curHocKy;
	DEALLOCATE curHocKy;
	SELECT * FROM @KetQuaHocTap;
END
GO
/****** Object:  StoredProcedure [dbo].[getThongTinSv]    Script Date: 10/10/2024 6:7:10 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[getThongTinSv] 
	@mssv VARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT * FROM [dbo].ThongTinSV WHERE mssv = @mssv;
END
GO
/****** Object:  StoredProcedure [dbo].[insertAccount]    Script Date: 10/10/2024 6:7:10 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[insertAccount]
	@userName varchar(50), @passWord varchar(255), @permission varchar(2)
AS
BEGIN
	SET NOCOUNT ON;

	BEGIN TRY 
		INSERT INTO dbo.Users(user_name, pass_word, permission)
		VALUES (@userName, @passWord, @permission);
	END TRY 
	BEGIN CATCH
		SELECT @@ERROR AS errorCode;
	END CATCH

	SELECT @@ERROR AS errorCode;
END
GO
/****** Object:  StoredProcedure [dbo].[insertGroupStudentAccount]    Script Date: 10/10/2024 6:7:10 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[insertGroupStudentAccount]
	@startMssv int, @endMssv int
AS
BEGIN
	SET NOCOUNT ON;

	DECLARE @errorCode int;
	DECLARE @passWord varchar(255);

	BEGIN TRAN
	BEGIN TRY
		WHILE @startMssv <= @endMssv
		BEGIN
			SET @passWord = CONVERT(VARCHAR(255), @startMssv);
			SET @passWord = CONVERT(VARCHAR(255), HashBytes('MD5', @passWord),2);
			SET @passWord = LOWER(@passWord);
			SET @passWord = CONVERT(VARCHAR(255), HashBytes('SHA2_256', @passWord),2);
			SET @passWord = LOWER(@passWord);
		
			INSERT INTO dbo.Users(user_name, pass_word, permission)
			VALUES(CONVERT(varchar(50), @startMssv), @passWord, 's');
			SET @startMssv = @startMssv + 1;
		END
	END TRY 
	BEGIN CATCH
		SET @errorCode = @@ERROR;

		IF  @errorCode <> 0
		BEGIN
			SELECT @errorCode AS errorCode;
			ROLLBACK TRAN
			RETURN;
		END

	END CATCH

	SET @errorCode = @@ERROR;
	COMMIT TRAN
	SELECT @errorCode AS errorCode;
END
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPane1', @value=N'[0E232FF0-B466-11cf-A24F-00AA00A3EFFF, 1.00]
Begin DesignProperties = 
   Begin PaneConfigurations = 
      Begin PaneConfiguration = 0
         NumPanes = 4
         Configuration = "(H (1[40] 4[20] 2[20] 3) )"
      End
      Begin PaneConfiguration = 1
         NumPanes = 3
         Configuration = "(H (1 [50] 4 [25] 3))"
      End
      Begin PaneConfiguration = 2
         NumPanes = 3
         Configuration = "(H (1 [50] 2 [25] 3))"
      End
      Begin PaneConfiguration = 3
         NumPanes = 3
         Configuration = "(H (4 [30] 2 [40] 3))"
      End
      Begin PaneConfiguration = 4
         NumPanes = 2
         Configuration = "(H (1 [56] 3))"
      End
      Begin PaneConfiguration = 5
         NumPanes = 2
         Configuration = "(H (2 [66] 3))"
      End
      Begin PaneConfiguration = 6
         NumPanes = 2
         Configuration = "(H (4 [50] 3))"
      End
      Begin PaneConfiguration = 7
         NumPanes = 1
         Configuration = "(V (3))"
      End
      Begin PaneConfiguration = 8
         NumPanes = 3
         Configuration = "(H (1[56] 4[18] 2) )"
      End
      Begin PaneConfiguration = 9
         NumPanes = 2
         Configuration = "(H (1 [75] 4))"
      End
      Begin PaneConfiguration = 10
         NumPanes = 2
         Configuration = "(H (1[66] 2) )"
      End
      Begin PaneConfiguration = 11
         NumPanes = 2
         Configuration = "(H (4 [60] 2))"
      End
      Begin PaneConfiguration = 12
         NumPanes = 1
         Configuration = "(H (1) )"
      End
      Begin PaneConfiguration = 13
         NumPanes = 1
         Configuration = "(V (4))"
      End
      Begin PaneConfiguration = 14
         NumPanes = 1
         Configuration = "(V (2))"
      End
      ActivePaneConfig = 0
   End
   Begin DiagramPane = 
      Begin Origin = 
         Top = 0
         Left = 0
      End
      Begin Tables = 
         Begin Table = "DangKyLop"
            Begin Extent = 
               Top = 6
               Left = 38
               Bottom = 136
               Right = 208
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "LopDK"
            Begin Extent = 
               Top = 6
               Left = 454
               Bottom = 136
               Right = 624
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "HocPhan"
            Begin Extent = 
               Top = 80
               Left = 262
               Bottom = 210
               Right = 432
            End
            DisplayFlags = 280
            TopColumn = 0
         End
      End
   End
   Begin SQLPane = 
   End
   Begin DataPane = 
      Begin ParameterDefaults = ""
      End
   End
   Begin CriteriaPane = 
      Begin ColumnWidths = 11
         Column = 1440
         Alias = 900
         Table = 1170
         Output = 720
         Append = 1400
         NewValue = 1170
         SortType = 1350
         SortOrder = 1410
         GroupBy = 1350
         Filter = 1350
         Or = 1350
         Or = 1350
         Or = 1350
      End
   End
End
' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'BangdiemSV'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPaneCount', @value=1 , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'BangdiemSV'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPane1', @value=N'[0E232FF0-B466-11cf-A24F-00AA00A3EFFF, 1.00]
Begin DesignProperties = 
   Begin PaneConfigurations = 
      Begin PaneConfiguration = 0
         NumPanes = 4
         Configuration = "(H (1[40] 4[20] 2[20] 3) )"
      End
      Begin PaneConfiguration = 1
         NumPanes = 3
         Configuration = "(H (1 [50] 4 [25] 3))"
      End
      Begin PaneConfiguration = 2
         NumPanes = 3
         Configuration = "(H (1 [50] 2 [25] 3))"
      End
      Begin PaneConfiguration = 3
         NumPanes = 3
         Configuration = "(H (4 [30] 2 [40] 3))"
      End
      Begin PaneConfiguration = 4
         NumPanes = 2
         Configuration = "(H (1 [56] 3))"
      End
      Begin PaneConfiguration = 5
         NumPanes = 2
         Configuration = "(H (2 [66] 3))"
      End
      Begin PaneConfiguration = 6
         NumPanes = 2
         Configuration = "(H (4 [50] 3))"
      End
      Begin PaneConfiguration = 7
         NumPanes = 1
         Configuration = "(V (3))"
      End
      Begin PaneConfiguration = 8
         NumPanes = 3
         Configuration = "(H (1[56] 4[18] 2) )"
      End
      Begin PaneConfiguration = 9
         NumPanes = 2
         Configuration = "(H (1 [75] 4))"
      End
      Begin PaneConfiguration = 10
         NumPanes = 2
         Configuration = "(H (1[66] 2) )"
      End
      Begin PaneConfiguration = 11
         NumPanes = 2
         Configuration = "(H (4 [60] 2))"
      End
      Begin PaneConfiguration = 12
         NumPanes = 1
         Configuration = "(H (1) )"
      End
      Begin PaneConfiguration = 13
         NumPanes = 1
         Configuration = "(V (4))"
      End
      Begin PaneConfiguration = 14
         NumPanes = 1
         Configuration = "(V (2))"
      End
      ActivePaneConfig = 0
   End
   Begin DiagramPane = 
      Begin Origin = 
         Top = 0
         Left = 0
      End
      Begin Tables = 
         Begin Table = "HocPhan"
            Begin Extent = 
               Top = 6
               Left = 38
               Bottom = 136
               Right = 208
            End
            DisplayFlags = 280
            TopColumn = 4
         End
         Begin Table = "KhoaVien"
            Begin Extent = 
               Top = 6
               Left = 246
               Bottom = 102
               Right = 416
            End
            DisplayFlags = 280
            TopColumn = 0
         End
      End
   End
   Begin SQLPane = 
   End
   Begin DataPane = 
      Begin ParameterDefaults = ""
      End
   End
   Begin CriteriaPane = 
      Begin ColumnWidths = 11
         Column = 1440
         Alias = 900
         Table = 1170
         Output = 720
         Append = 1400
         NewValue = 1170
         SortType = 1350
         SortOrder = 1410
         GroupBy = 1350
         Filter = 1350
         Or = 1350
         Or = 1350
         Or = 1350
      End
   End
End
' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'DsHP'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPaneCount', @value=1 , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'DsHP'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPane1', @value=N'[0E232FF0-B466-11cf-A24F-00AA00A3EFFF, 1.00]
Begin DesignProperties = 
   Begin PaneConfigurations = 
      Begin PaneConfiguration = 0
         NumPanes = 4
         Configuration = "(H (1[40] 4[20] 2[20] 3) )"
      End
      Begin PaneConfiguration = 1
         NumPanes = 3
         Configuration = "(H (1 [50] 4 [25] 3))"
      End
      Begin PaneConfiguration = 2
         NumPanes = 3
         Configuration = "(H (1 [50] 2 [25] 3))"
      End
      Begin PaneConfiguration = 3
         NumPanes = 3
         Configuration = "(H (4 [30] 2 [40] 3))"
      End
      Begin PaneConfiguration = 4
         NumPanes = 2
         Configuration = "(H (1 [56] 3))"
      End
      Begin PaneConfiguration = 5
         NumPanes = 2
         Configuration = "(H (2 [66] 3))"
      End
      Begin PaneConfiguration = 6
         NumPanes = 2
         Configuration = "(H (4 [50] 3))"
      End
      Begin PaneConfiguration = 7
         NumPanes = 1
         Configuration = "(V (3))"
      End
      Begin PaneConfiguration = 8
         NumPanes = 3
         Configuration = "(H (1[56] 4[18] 2) )"
      End
      Begin PaneConfiguration = 9
         NumPanes = 2
         Configuration = "(H (1 [75] 4))"
      End
      Begin PaneConfiguration = 10
         NumPanes = 2
         Configuration = "(H (1[66] 2) )"
      End
      Begin PaneConfiguration = 11
         NumPanes = 2
         Configuration = "(H (4 [60] 2))"
      End
      Begin PaneConfiguration = 12
         NumPanes = 1
         Configuration = "(H (1) )"
      End
      Begin PaneConfiguration = 13
         NumPanes = 1
         Configuration = "(V (4))"
      End
      Begin PaneConfiguration = 14
         NumPanes = 1
         Configuration = "(V (2))"
      End
      ActivePaneConfig = 0
   End
   Begin DiagramPane = 
      Begin Origin = 
         Top = 0
         Left = 0
      End
      Begin Tables = 
         Begin Table = "LopSV"
            Begin Extent = 
               Top = 6
               Left = 38
               Bottom = 119
               Right = 208
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "SinhVien"
            Begin Extent = 
               Top = 6
               Left = 246
               Bottom = 136
               Right = 416
            End
            DisplayFlags = 280
            TopColumn = 2
         End
      End
   End
   Begin SQLPane = 
   End
   Begin DataPane = 
      Begin ParameterDefaults = ""
      End
   End
   Begin CriteriaPane = 
      Begin ColumnWidths = 11
         Column = 1440
         Alias = 900
         Table = 1170
         Output = 720
         Append = 1400
         NewValue = 1170
         SortType = 1350
         SortOrder = 1410
         GroupBy = 1350
         Filter = 1350
         Or = 1350
         Or = 1350
         Or = 1350
      End
   End
End
' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'DsLopSV'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPaneCount', @value=1 , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'DsLopSV'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPane1', @value=N'[0E232FF0-B466-11cf-A24F-00AA00A3EFFF, 1.00]
Begin DesignProperties = 
   Begin PaneConfigurations = 
      Begin PaneConfiguration = 0
         NumPanes = 4
         Configuration = "(H (1[40] 4[20] 2[20] 3) )"
      End
      Begin PaneConfiguration = 1
         NumPanes = 3
         Configuration = "(H (1 [50] 4 [25] 3))"
      End
      Begin PaneConfiguration = 2
         NumPanes = 3
         Configuration = "(H (1 [50] 2 [25] 3))"
      End
      Begin PaneConfiguration = 3
         NumPanes = 3
         Configuration = "(H (4 [30] 2 [40] 3))"
      End
      Begin PaneConfiguration = 4
         NumPanes = 2
         Configuration = "(H (1 [56] 3))"
      End
      Begin PaneConfiguration = 5
         NumPanes = 2
         Configuration = "(H (2 [66] 3))"
      End
      Begin PaneConfiguration = 6
         NumPanes = 2
         Configuration = "(H (4 [50] 3))"
      End
      Begin PaneConfiguration = 7
         NumPanes = 1
         Configuration = "(V (3))"
      End
      Begin PaneConfiguration = 8
         NumPanes = 3
         Configuration = "(H (1[56] 4[18] 2) )"
      End
      Begin PaneConfiguration = 9
         NumPanes = 2
         Configuration = "(H (1 [75] 4))"
      End
      Begin PaneConfiguration = 10
         NumPanes = 2
         Configuration = "(H (1[66] 2) )"
      End
      Begin PaneConfiguration = 11
         NumPanes = 2
         Configuration = "(H (4 [60] 2))"
      End
      Begin PaneConfiguration = 12
         NumPanes = 1
         Configuration = "(H (1) )"
      End
      Begin PaneConfiguration = 13
         NumPanes = 1
         Configuration = "(V (4))"
      End
      Begin PaneConfiguration = 14
         NumPanes = 1
         Configuration = "(V (2))"
      End
      ActivePaneConfig = 0
   End
   Begin DiagramPane = 
      Begin Origin = 
         Top = 0
         Left = 0
      End
      Begin Tables = 
         Begin Table = "LopSV"
            Begin Extent = 
               Top = 6
               Left = 38
               Bottom = 119
               Right = 208
            End
            DisplayFlags = 280
            TopColumn = 0
         End
         Begin Table = "SinhVien"
            Begin Extent = 
               Top = 6
               Left = 246
               Bottom = 136
               Right = 416
            End
            DisplayFlags = 280
            TopColumn = 8
         End
      End
   End
   Begin SQLPane = 
   End
   Begin DataPane = 
      Begin ParameterDefaults = ""
      End
      Begin ColumnWidths = 11
         Width = 284
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
         Width = 1500
      End
   End
   Begin CriteriaPane = 
      Begin ColumnWidths = 11
         Column = 1440
         Alias = 900
         Table = 1170
         Output = 720
         Append = 1400
         NewValue = 1170
         SortType = 1350
         SortOrder = 1410
         GroupBy = 1350
         Filter = 1350
         Or = 1350
         Or = 1350
         Or = 1350
      End
   End
End
' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'ThongTinSV'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_DiagramPaneCount', @value=1 , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'VIEW',@level1name=N'ThongTinSV'
GO
USE [master]
GO
ALTER DATABASE [StudentManager] SET  READ_WRITE 
GO
