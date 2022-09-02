import java.io.Serializable;

     public class Vinho implements Serializable {
     private static final long serialVersionUID = 7100179587555243994L;
     private String nome;
     private String tipo;
     private String descricao;

public class Serializer {
      public static void main(String... args) throws Exception { 
        Vinhovinho = new Vinho();
        vinho.setNome("Malbec");
        vinho.setTipo(“Rose”);
    
       FileOutputStream fOut = new FileOutputStream("C:\\vinhos.ser");
       ObjectOutputStream oOut = new ObjectOutputStream(fOut);
        oOut.writeObject(vinho);
       oOut.close();
        System.out.println("Objeto serializado.");
}
}
 public class Deserializer {
     public static void main(String... args) throws Exception {
       FileInputStream fOut= new FileInputStream("C:\\vinhos.ser");
      ObjectInputStream oOut= new ObjectInputStream(fOut);
       Vinhovinho = (Vinho) oOut.readObject();
       oOut.close();
     
       System.out.println("Objeto deserializado.");
     }
