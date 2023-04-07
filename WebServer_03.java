public class ExemploServico {
    
    public String saudacao(String nome) {
        return "Olá, " + nome + "!";
    }
    
    public int soma(int a, int b) {
        return a + b;
    }
    
    public int subtracao(int a, int b) {
        return a - b;
    }
    
    public String saudacaoHora(String nome) {
        Calendar cal = Calendar.getInstance();
        int hora = cal.get(Calendar.HOUR_OF_DAY);
        if (hora < 12) {
            return "Bom dia, " + nome + "!";
        } else if (hora < 18) {
            return "Boa tarde, " + nome + "!";
        } else {
            return "Boa noite, " + nome + "!";
        }
    }
}

import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebService;

@WebService
public class ServicoSOAP {
    
    private ExemploServico exemploServico = new ExemploServico();
    
    @WebMethod
    public String saudacao(@WebParam(name = "nome") String nome) {
        return exemploServico.saudacao(nome);
    }
    
    @WebMethod
    public int soma(@WebParam(name = "a") int a, @WebParam(name = "b") int b) {
        return exemploServico.soma(a, b);
    }
    
    @WebMethod
    public int subtracao(@WebParam(name = "a") int a, @WebParam(name = "b") int b) {
        return exemploServico.subtracao(a, b);
    }
    
    @WebMethod
    public String saudacaoHora(@WebParam(name = "nome") String nome) {
        return exemploServico.saudacaoHora(nome);
    }
}

import org.apache.cxf.jaxws.JaxWsServerFactoryBean;

public class ServidorSOAP {

    public static void main(String[] args) {
      
       
