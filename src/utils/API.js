import axios from "axios";

export default{
	predictImage: function(url){
		return axios.post("/api/books", url)
	}
}