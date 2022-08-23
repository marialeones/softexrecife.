public class App {
    public static void main(String[] args) throws Exception {
       Celular celular1 = new Celular(); 
       celular1.nome = "Motorola ";
       celular1.tamanhoTela = 6.1f;
       celular1.espacoArmaz = 256;
       celular1.sistemaOpera = "Android";

       System.out.format("Celular: %s com tela de %.1f, com %dgb e Sistema Operacional: %s \n ", celular1.nome, celular1.tamanhoTela, celular1.espacoArmaz, celular1.sistemaOpera);
      
       Celular celular2 = new Celular();
       celular2.nome = "Galaxy Note 20 Ultra ";
       celular2.tamanhoTela = 6.9f;
       celular2.espacoArmaz = 256;
       celular2.sistemaOpera = "Android";

       System.out.format("Celular: %s com tela de %.1f, com %dgb e Sistema Operacional: %s \n ", celular2.nome, celular2.tamanhoTela, celular2.espacoArmaz, celular2.sistemaOpera);

       Celular celular3 = new Celular();
       celular3.nome = "Iphone 12 ";
       celular3.tamanhoTela = 5.9f;
       celular3.espacoArmaz = 128;
       celular3.sistemaOpera = "iOS";

       System.out.format("Celular: %s com tela de %.1f, com %dgb e Sistema Operacional: %s \n ", celular3.nome, celular3.tamanhoTela, celular3.espacoArmaz, celular3.sistemaOpera);
 
    }

}