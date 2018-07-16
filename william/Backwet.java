package org.william;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


public class Backwet extends HttpServlet{

    public void doGet(HttpServletRequest request,HttpServletResponse response) throws ServletException,IOException{
        doPost(request,response);
    }

    public void doPost(HttpServletRequest request,HttpServletResponse response) throws ServletException,IOException{
        String json1 = "";
        String json2 = "";
        String state = request.getParameter("state");
        String code  = request.getParameter("code");
        String httpurl = "https://api.weixin.qq.com/sns/oauth2/access_token";
    }
}
