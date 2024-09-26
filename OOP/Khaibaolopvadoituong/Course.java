public class Course {
    public String courseID;
    public String courseName;
    public int credits;
    public Map<Student, Double> studentScores;

    public void addStudent(Student student);
    public void removeStudent(Student student);
    public void assignGrade(Student student, double grade);
}
