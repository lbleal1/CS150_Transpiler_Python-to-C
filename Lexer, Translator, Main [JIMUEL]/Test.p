DEF INT add(INT x, INT y) {
	INT sum = x + y
	RETURN sum
}

DEF INT MAIN(){
	STRING temp = "string_test hehe"
	INT tempI = 6.24
	
	WRITE("I'M MAKING")
	WRITE("THE P LANGUAGE :D")

	IF tempI <= 10 AND tempI > 5 THEN{
		tempI+=3
	}
	ELSIF tempI == 9 THEN{
		WRITE("NINE LIVES BOI!")
	}
	ELSE{
		WRITE("SAD.")
	}

	WHILE (tempI < 15){
		WRITE("I'm almost there...")
		tempI +=1
		IF tempI == 12 THEN{
			SKIP
		}
		ELSIF tempI == 13 THEN{
			STOP
		}
	}

}