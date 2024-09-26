public class CourseManager {
    public List<Course> courses;

    public void addCourse(Course course);
    public void removeCourse(String courseID);
    public void updateCourse(Course course);
    public List<Course> listCourses();
}
