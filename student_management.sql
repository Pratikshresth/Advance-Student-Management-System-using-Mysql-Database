-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 03, 2020 at 03:14 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `computing`
--

CREATE TABLE `computing` (
  `ID` int(11) NOT NULL,
  `Section` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `computing`
--

INSERT INTO `computing` (`ID`, `Section`) VALUES
(1, 'CS19A');

-- --------------------------------------------------------

--
-- Table structure for table `credentials`
--

CREATE TABLE `credentials` (
  `ID` int(11) NOT NULL,
  `Username` varchar(100) DEFAULT NULL,
  `Password` varchar(100) DEFAULT NULL,
  `Full_Name` varchar(100) NOT NULL,
  `E_mail` varchar(100) NOT NULL,
  `Authority` enum('Admin','User') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `credentials`
--

INSERT INTO `credentials` (`ID`, `Username`, `Password`, `Full_Name`, `E_mail`, `Authority`) VALUES
(1, 'Admin', 'Admin@123', 'Admin', 'admin@gmail.com', 'Admin'),
(2, 'User', 'User@1234', 'Normal User', 'nuser@gmail.com', 'User');

-- --------------------------------------------------------

--
-- Table structure for table `ethical`
--

CREATE TABLE `ethical` (
  `ID` int(11) NOT NULL,
  `Section` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ethical`
--

INSERT INTO `ethical` (`ID`, `Section`) VALUES
(1, 'ES19A');

-- --------------------------------------------------------

--
-- Table structure for table `fees`
--

CREATE TABLE `fees` (
  `ID` int(11) NOT NULL,
  `Student_ID` int(11) DEFAULT NULL,
  `Semester` varchar(100) DEFAULT NULL,
  `Fee_Paid` int(11) DEFAULT NULL,
  `Discount` int(11) DEFAULT NULL,
  `Fee_Due` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `grades`
--

CREATE TABLE `grades` (
  `ID` int(11) NOT NULL,
  `Student_ID` int(11) DEFAULT NULL,
  `Modules` varchar(100) DEFAULT NULL,
  `Marks_Obtained` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `new_students`
--

CREATE TABLE `new_students` (
  `ID` int(11) NOT NULL,
  `First_Name` varchar(100) DEFAULT NULL,
  `Last_Name` varchar(100) DEFAULT NULL,
  `City` varchar(100) DEFAULT NULL,
  `Zip_Code` int(11) DEFAULT NULL,
  `State` varchar(100) DEFAULT NULL,
  `Gender` varchar(100) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Contact` varchar(15) DEFAULT NULL,
  `DOB` varchar(100) DEFAULT NULL,
  `Program` varchar(100) DEFAULT NULL,
  `Section` varchar(100) DEFAULT NULL,
  `College_ID` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `new_students`
--

INSERT INTO `new_students` (`ID`, `First_Name`, `Last_Name`, `City`, `Zip_Code`, `State`, `Gender`, `Email`, `Contact`, `DOB`, `Program`, `Section`, `College_ID`) VALUES
(1, 'Pratik', 'Shrestha', 'Lalitpur', 44700, 'Bagmati Pradesh', 'Male', 'pratik@gmail.com', '9860580195', '11/26/1999', 'BSc(Hons) Ethical Hacking and Cybersecurity', 'Select', 'STW-1001'),
(2, 'Prasanna', 'Shrestha', 'Lalitpur', 44700, 'Bagmati Pradesh', 'Male', 'prasanna@gmail.com', '9841785214', '01/11/2000', 'BSc(Hons) Computing', 'CS19A', 'STW-1002');

-- --------------------------------------------------------

--
-- Table structure for table `user_detail`
--

CREATE TABLE `user_detail` (
  `ID` int(11) NOT NULL,
  `Username` varchar(100) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `Type` varchar(100) NOT NULL,
  `Last_Logged_In` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_detail`
--

INSERT INTO `user_detail` (`ID`, `Username`, `Password`, `Type`, `Last_Logged_In`) VALUES
(1, 'Admin', 'Admin@123', 'Admin', '03/09/2020 06:55:15:PM'),
(2, 'User', 'User@1234', 'User', '03/09/2020 03:41:51:PM');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `computing`
--
ALTER TABLE `computing`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `Section` (`Section`);

--
-- Indexes for table `credentials`
--
ALTER TABLE `credentials`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `Username` (`Username`);

--
-- Indexes for table `ethical`
--
ALTER TABLE `ethical`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `Section` (`Section`);

--
-- Indexes for table `fees`
--
ALTER TABLE `fees`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Student_ID` (`Student_ID`);

--
-- Indexes for table `grades`
--
ALTER TABLE `grades`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Student_ID` (`Student_ID`);

--
-- Indexes for table `new_students`
--
ALTER TABLE `new_students`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `Email` (`Email`),
  ADD UNIQUE KEY `Contact` (`Contact`),
  ADD UNIQUE KEY `College_ID` (`College_ID`);

--
-- Indexes for table `user_detail`
--
ALTER TABLE `user_detail`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `Username` (`Username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `computing`
--
ALTER TABLE `computing`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `credentials`
--
ALTER TABLE `credentials`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `ethical`
--
ALTER TABLE `ethical`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `fees`
--
ALTER TABLE `fees`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `grades`
--
ALTER TABLE `grades`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `new_students`
--
ALTER TABLE `new_students`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user_detail`
--
ALTER TABLE `user_detail`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `fees`
--
ALTER TABLE `fees`
  ADD CONSTRAINT `fees_ibfk_1` FOREIGN KEY (`Student_ID`) REFERENCES `new_students` (`ID`);

--
-- Constraints for table `grades`
--
ALTER TABLE `grades`
  ADD CONSTRAINT `grades_ibfk_1` FOREIGN KEY (`Student_ID`) REFERENCES `new_students` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
