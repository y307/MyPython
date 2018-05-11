unit uBarCoding;

interface

uses
	SysUtils;

const
	EAN_izqA:array[0..9]of PChar=
			('0001101','0011001','0010011','0111101','0100011',
				'0110001','0101111','0111011','0110111','0001011');
	EAN_izqB:array[0..9]of PChar=
			('0100111','0110011','0011011','0100001','0011101',
				'0111001','0000101','0010001','0001001','0010111');
	EAN_dcha:array[0..9]of PChar=
			('1110010','1100110','1101100','1000010','1011100',
				'1001110','1010000','1000100','1001000','1110100');
	CodificaIzq:array[0..9]of PChar=
			('AAAAA','ABABB','ABBAB','ABBBA','BAABB',
				'BBAAB','BBBAA','BABAB','BABBA','BBABA');

//function GetLastDigit(num: string):Byte;
function _GetLastDigit(aNum:string):Byte;

implementation

{
function GetLastDigit(num: string): Byte;
var
	i,N : byte;
	sum : integer;
	flag : byte;
begin
	sum:=0;
	N:=Length(num)-1;
	for i:=1 to N do
	begin
		if (i mod 2)=0 then
		begin
			if N=12 then
				sum:=sum+StrToInt(num[i])*3
			else
				sum:=sum+StrToInt(num[i]);
		end
		else
		begin
			if N=12 then
				sum:=sum+StrToInt(num[i])
			else
				sum:=sum+StrToInt(num[i])*3;
		end;
	end;
	if sum>99 then
		Flag:=10-(sum mod 100)
	else
		Flag:=10-(sum mod 10);
	if Flag=10 then Flag:=0;
	Result:= Flag;
end;
}

function _GetLastDigit(aNum:string):Byte;
var
	vPos,vFact,vSum:Integer;
begin
	vPos:=12;
	vSum:=0;
	vFact:=3;
	while vPos>0 do
	begin
		vSum:=vSum+StrToInt(aNum[vPos])*vFact;
		vFact:=4-vFact;
		Dec(vPos);
	end;

	Result:=vSum mod 10;
	if Result<>0 then
		Result:=10-Result;
end;

end.
