package org.william;

import java.io.BufferedReader;
import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


public class Dati extends HttpServlet{

    public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException,IOException{
        doPost(request,response);
    }

    public void doPost(HttpServletRequest request,HttpServletResponse response) throws ServletException,IOException{

        response.setContentType("text/plain;charset=utf-8");
        String user_id = request.getParameter("user_id");
        String score   = request.getParameter("score");
        int    I_score = Integer.parseInt(score);
        String time    = request.getParameter("time");

        try{
            DBConnection dbconnection = new DBConnection();
            String sql = "insert into result values('"+user_id+"',"+I_score+",'"+time+"');";
            System.out.println(sql);
            dbconnection.execute(sql);

        } catch(Exception e){
            e.printStackTrace();
        }
    }
}
