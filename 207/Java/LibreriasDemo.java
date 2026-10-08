// Situación: se registra un terreno cuadrado con un área aleatoria
// y se calcula cuánto mide cada lado.
import java.util.Random;
import java.time.LocalDate;

public class LibreriasDemo {

    public static void main(String[] args) {

        Random rand = new Random();
        int area = rand.nextInt(100) + 1;    // Random: área del terreno en m2

        double lado = Math.sqrt(area);       // Math: lado = raíz cuadrada del área

        LocalDate fecha = LocalDate.now();   // LocalDate: fecha del registro

        System.out.println("Área del terreno: " + area + " m2");
        System.out.printf("Lado del terreno: %.2f m%n", lado);
        System.out.println("Fecha de registro: " + fecha);
    }
}
