public class StudentManager {
    public List<Student> students;

    public void addStudent(Student student);
    public void removeStudent(String studentID);
    public void updateStudent(Student student);
    public List<Student> listStudents();
    public List<Student> filterByGPA(double minGPA);
}
