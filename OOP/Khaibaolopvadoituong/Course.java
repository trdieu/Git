public class Course {
    public String courseID;
    public String courseName;
    public int credits;
    public Map<Student, Double> studentScores;

    
    public Course(String courseID, String courseName, int credits) {
        this.courseID = courseID;
        this.courseName = courseName;
        this.credits = credits;
        this.studentScores = new HashMap<>();
    }
