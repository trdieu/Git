public class FileManager {

    public void saveData(Object data, String fileName) throws IOException;
    public Object loadData(String fileName) throws IOException, ClassNotFoundException;
}

