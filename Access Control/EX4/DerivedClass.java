// mypackage/DerivedClass.java
package mypackage;

public class DerivedClass extends BaseClass {
    public void callProtectedMethod() {
        protectedMethod(); // Calling the protected method from BaseClass
    }

    public static void main(String[] args) {
        DerivedClass obj = new DerivedClass();
        obj.callProtectedMethod();
    }
}