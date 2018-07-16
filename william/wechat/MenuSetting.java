package org.william.wechat;

import org.json.JSONException; 
import org.json.JSONObject; 

public class MenuSetting {

	public static String appId = "wxece26bff13e17f01";
    public static String appSecret= "2229d866e4deef0ff76a0033fec0e43d"; 
    
	public static void main(String[] args) throws JSONException {
		add();
		//delete();
	}

    public static String getAccessToken() throws JSONException{
        NetWorkHelper netHelper = new NetWorkHelper();
        String Url = String.format("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s",appId,appSecret);
        String result = netHelper.getHttpsResponse(Url,"");
        System.out.println(result);
        //JSONObject json = JSONObject.fromObject(result);
        JSONObject json = new JSONObject(result);
        return  json.getString("access_token");
    }
    
    public static void delete() throws JSONException{
    		String s = getAccessToken();
        NetWorkHelper netHelper = new NetWorkHelper();
        String Url = String.format("https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s", s);
        String result = netHelper.getHttpsResponse(Url,"");
        System.out.println(result);
    }
    
    public static void add() throws JSONException{
    		String s = getAccessToken();
        NetWorkHelper netHelper = new NetWorkHelper();
        String json = "{"
        		+ "\"button\":["
        		+ "{"
        		+ "\"name\":\"��ʷ����\","
        		+ "\"sub_button\":["
        		+ "{"	
                + "\"type\":\"view\","
                + "\"name\":\"��ʼ����\","
                + "\"url\":\"http://pv4z4x.natappfree.cc/info/qa.html\""
                + "}]"
        		+ "},"
        		+ "{"
        		+ "\"name\":\"�ҵ�����\","
        		+ "\"sub_button\":["
        		+ "{"
        		+ "\"type\":\"view\","
        		+ "\"name\":\"�ҵĳɼ�\","
        		+ "\"url\":\"http://pv4z4x.natappfree.cc/info/score.html\""
        		+ "},"
        		+ "{"	
                + "\"type\":\"view\","
                + "\"name\":\"��������\","
                + "\"url\":\"http://www.hnust.cn\""
             	+ "},"
             	 + "{"
                 + "\"type\":\"view\","
                 + "\"name\":\"�༶����\","
                 + "\"url\":\"http://www.hnust.cn\""
              	+ "},"
             	+ "{"
                + "\"type\":\"view\","
                + "\"name\":\"����\","
                + "\"url\":\"http://www.hnust.cn\""
             	+ "}]"
        		+ "},"
        		+ "{"
        		+ "\"name\":\"��������\","
        		+ "\"sub_button\":["
        		+ "{"	
                + "\"type\":\"view\","
                + "\"name\":\"������\","
                + "\"url\":\"http://www.hnust.cn/\""
                + "},"
             	+ "{"
                + "\"type\":\"view\","
                + "\"name\":\"��ϵ��\","
                + "\"url\":\"http://www.hnust.cn/\""
             	+ "}]"
        		+ "}]"
        		+ "}";
        System.out.println(json);
         
        String Url = String.format("https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s", s);      
        String result = netHelper.getHttpsResponsePostBody(Url, "POST", json);
        System.out.println(result);
    }
    
}

