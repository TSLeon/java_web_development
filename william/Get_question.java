package org.william;

import java.io.BufferedReader;

import java.util.Random;
import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.json.JSONException;
import org.json.JSONObject;
import java.util.ArrayList;
import java.sql.ResultSet;

public class Get_question extends HttpServlet{

    public void doGet(HttpServletRequest request,HttpServletResponse response) throws ServletException,IOException {
        doPost(request,response);
    }

    public void doPost(HttpServletRequest request,HttpServletResponse response) throws ServletException,IOException{

        response.setContentType("text/plain;charset=utf-8");

        try{
            DBConnection dbconnection = new DBConnection();
            String sql = "select * from question;";

            ResultSet rs = dbconnection.executeQuery(sql);
            ArrayList<Question> list = new ArrayList();
            while(rs.next())
            {
                int question_id = rs.getInt(1);
                String question_text = rs.getString(2);
                String option_one    = rs.getString(3);
                String option_twe    = rs.getString(4);
                String option_three  = rs.getString(5);
                String option_four   = rs.getString(6);
                String answer        = rs.getString(7);
                Question t = new Question(question_id,question_text,option_one,option_twe,option_three,option_four,answer);
                list.add(t);
            }
            dbconnection.close();

            response.setCharacterEncoding("utf-8");
            PrintWriter out = response.getWriter();
            JSONObject  obj = new JSONObject();
            JSONObject  obj1 = new JSONObject();
            JSONObject  obj2 = new JSONObject();
            JSONObject  obj3 = new JSONObject();
            JSONObject  obj4 = new JSONObject();
            Question t =  new Question();

            Random r = new Random();
            int j = 0;
            int[] ques = {-1,-1,-1,-1};
            while(j < 4)
            {
                int randnumber = r.nextInt(list.size());
                int i = 0;
                while(i < 4)
                {
                    if(ques[i] == randnumber)
                        break;
                    i++;
                }
                if(i == 4)
                {
                    ques[j] = randnumber;
                    j++;
                }
            }

            t = list.get(ques[0]);
            obj1.put("question_id",t.getId());
            obj1.put("question_text",t.getQuestion());
            obj1.put("A",t.getOption_one());
            obj1.put("B",t.getOption_twe());
            obj1.put("C",t.getOption_three());
            obj1.put("D",t.getOption_four());
            obj1.put("answer",t.getAnswer());

            t = list.get(ques[1]);
            obj2.put("question_id",t.getId());
            obj2.put("question_text",t.getQuestion());
            obj2.put("A",t.getOption_one());
            obj2.put("B",t.getOption_twe());
            obj2.put("C",t.getOption_three());
            obj2.put("D",t.getOption_four());
            obj2.put("answer",t.getAnswer());

            t = list.get(ques[2]);
            obj3.put("question_id",t.getId());
            obj3.put("question_text",t.getQuestion());
            obj3.put("A",t.getOption_one());
            obj3.put("B",t.getOption_twe());
            obj3.put("C",t.getOption_three());
            obj3.put("D",t.getOption_four());
            obj3.put("answer",t.getAnswer());

            t = list.get(ques[3]);
            obj4.put("question_id",t.getId());
            obj4.put("question_text",t.getQuestion());
            obj4.put("A",t.getOption_one());
            obj4.put("B",t.getOption_twe());
            obj4.put("C",t.getOption_three());
            obj4.put("D",t.getOption_four());
            obj4.put("answer",t.getAnswer());

            obj.put("result","ok");
            obj.put("question_one",obj1);
            obj.put("question_twe",obj2);
            obj.put("question_three",obj3);
            obj.put("question_four",obj4);
            out.print(obj.toString());
            out.flush();
            out.close();
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}
