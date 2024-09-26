public class Student {
    public String studentID;
    public String name;
    public LocalDate dob;
    public double gpa;
    public List<Course> registeredCourses;

    public void addCourse(Course course);
    public void removeCourse(Course course);
    public double calculateGPA();
}
