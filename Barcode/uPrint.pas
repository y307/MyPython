unit uPrint;

interface

uses
	Windows,Messages,SysUtils,ExtCtrls,Classes,Graphics,Controls,Forms,Dialogs,
	StrUtils,StdCtrls,ComCtrls,uBarCoding,QuickRpt,Qrctrls,Menus,uMisc;

type

{
	TCoupon=Record
		LastNum:Integer;
		Series:string[2];
	end;
}

	T_TalonType=(tt_0,tt_1,ttTPV,ttTPV3,ttTPV4);

	T_TalonId=record
		TalonType:Byte;
		ValueType:Byte;
	end;

	TForm1 = class(TForm)
		StatusBar1: TStatusBar;
		QuickRep1: TQuickRep;
		TitleBand1: TQRBand;
		QRImage1: TQRImage;
		QRImage2: TQRImage;
		QRImage3: TQRImage;
		QRImage4: TQRImage;
		QRImage5: TQRImage;
		QRLabel1: TQRLabel;
		QRLabel2: TQRLabel;
		QRLabel3: TQRLabel;
		QRLabel4: TQRLabel;
		QRLabel5: TQRLabel;
		QRLabel6: TQRLabel;
		QRLabel7: TQRLabel;
		QRLabel8: TQRLabel;
		QRLabel9: TQRLabel;
		QRLabel10: TQRLabel;
		MainMenu1: TMainMenu;
		mmOptions: TMenuItem;
		mmiPrinter: TMenuItem;
		mmExit: TMenuItem;
		QRLabel11: TQRLabel;
		QRImage6: TQRImage;
		QRLabel12: TQRLabel;
		QRLabel13: TQRLabel;
		QRImage7: TQRImage;
		QRLabel14: TQRLabel;
		QRLabel15: TQRLabel;
		QRImage8: TQRImage;
		QRLabel16: TQRLabel;
		QRLabel17: TQRLabel;
		QRImage9: TQRImage;
		QRLabel18: TQRLabel;
		QRLabel19: TQRLabel;
		QRImage10: TQRImage;
		QRLabel20: TQRLabel;
		QRLabel21: TQRLabel;
		QRImage11: TQRImage;
		QRLabel22: TQRLabel;
		QRLabel23: TQRLabel;
		QRImage12: TQRImage;
		QRLabel24: TQRLabel;
		QRLabel25: TQRLabel;
		QRImage13: TQRImage;
		QRLabel26: TQRLabel;
		QRLabel27: TQRLabel;
		QRImage14: TQRImage;
		QRLabel28: TQRLabel;
		QRLabel29: TQRLabel;
		QRImage15: TQRImage;
		QRLabel30: TQRLabel;
		QRLabel31: TQRLabel;
		QRImage16: TQRImage;
		QRLabel32: TQRLabel;
		QRLabel33: TQRLabel;
		QRImage17: TQRImage;
		QRLabel34: TQRLabel;
		QRLabel35: TQRLabel;
		QRImage18: TQRImage;
		QRLabel36: TQRLabel;
		QRLabel37: TQRLabel;
		QRImage19: TQRImage;
		QRLabel38: TQRLabel;
		QRLabel39: TQRLabel;
		QRImage20: TQRImage;
		QRLabel40: TQRLabel;
		QRLabel41: TQRLabel;
		QRImage21: TQRImage;
		QRLabel42: TQRLabel;
		QRLabel43: TQRLabel;
		QRImage22: TQRImage;
		QRLabel44: TQRLabel;
		QRLabel45: TQRLabel;
		QRImage23: TQRImage;
		QRLabel46: TQRLabel;
		QRLabel47: TQRLabel;
		QRImage24: TQRImage;
		QRLabel48: TQRLabel;
		QRLabel49: TQRLabel;
		QRImage25: TQRImage;
		QRLabel50: TQRLabel;
		QRLabel51: TQRLabel;
		QRImage26: TQRImage;
		QRLabel52: TQRLabel;
		QRLabel53: TQRLabel;
		QRImage27: TQRImage;
		QRLabel54: TQRLabel;
		QRLabel55: TQRLabel;
		QRImage28: TQRImage;
		QRLabel56: TQRLabel;
		QRLabel57: TQRLabel;
		QRImage29: TQRImage;
		QRLabel58: TQRLabel;
		QRLabel59: TQRLabel;
		QRImage30: TQRImage;
		QRLabel60: TQRLabel;
		edSheets: TEdit;
		Label1: TLabel;
		edSeries: TEdit;
		Label2: TLabel;
		btnPrint: TButton;
		Label6: TLabel;
		edFromNum: TEdit;
		chbView: TCheckBox;
		Label9: TLabel;
		edListOnly1: TEdit;
		Label8: TLabel;
		edFromTop: TEdit;
		UpDown2: TUpDown;
		Label3: TLabel;
		edListOnly2: TEdit;
    chbLowerOut: TCheckBox;
    btnFromNumClear: TButton;
    btnListOnlyClear: TButton;
    ChbShowProgress: TCheckBox;
    chbMirror: TCheckBox;
    chbPart: TCheckBox;
    edPart: TEdit;
    btnPartClear: TButton;
    Label4: TLabel;
    edMonth: TEdit;
    Label5: TLabel;
    QRL1: TQRLabel;
    QRL2: TQRLabel;
    QRL3: TQRLabel;
    QRL4: TQRLabel;
    QRL5: TQRLabel;
    QRL6: TQRLabel;
    QRL7: TQRLabel;
    QRL8: TQRLabel;
    QRL9: TQRLabel;
    QRL10: TQRLabel;
    QRL11: TQRLabel;
    QRL12: TQRLabel;
    QRL13: TQRLabel;
    QRL14: TQRLabel;
    QRL15: TQRLabel;
    QRL16: TQRLabel;
    QRL17: TQRLabel;
    QRL18: TQRLabel;
		QRL19: TQRLabel;
		QRL20: TQRLabel;
		QRL21: TQRLabel;
		QRL22: TQRLabel;
		QRL23: TQRLabel;
		QRL24: TQRLabel;
		QRL25: TQRLabel;
		QRL26: TQRLabel;
		QRL27: TQRLabel;
		QRL28: TQRLabel;
		QRL29: TQRLabel;
		QRL30: TQRLabel;
    edSkip: TEdit;
    Label7: TLabel;
    btnSkipClear: TButton;
		procedure FormShow(Sender: TObject);
		procedure FormClose(Sender: TObject; var Action: TCloseAction);
		procedure DrawCode(aMatrix: string; aItNum: Byte; aInvisible:Boolean=False);
		procedure mmiPrinterClick(Sender: TObject);
		procedure mmExitClick(Sender: TObject);
		procedure FormClick(Sender: TObject);
		procedure edSheetsChange(Sender: TObject);
		procedure cmbTypeChange(Sender: TObject);
		procedure btnPrintClick(Sender: TObject);
		procedure btnFromNumClearClick(Sender: TObject);
		procedure btnListOnlyClearClick(Sender: TObject);
		procedure chbMirrorClick(Sender: TObject);
		procedure btnPartClearClick(Sender: TObject);
    procedure btnSkipClearClick(Sender: TObject);
	private
		procedure SetMassOfQR;
		{ Private declarations }
	public
		{ Public declarations }
		procedure Coding(aNum : string; aItemNumb: Byte; aInvisible:Boolean=False);
	end;

const
	TALONS_ON_LIST=30;
	SERIES_LENGTH=1000000;
	c_UkrString='АБВГДЕЄЖЗИІЙКЛМНОПРСТУФХЦЧШЩЮЯ';
	c_Sec='main';

var
	Form1: TForm1;
	//v_File: File of TCoupon;
	//v_Talon:TCoupon;
	v_Ser:Integer;
	v_Month:string;
	v_LastNo:Integer;
	v_BarCode:string[13];
	v_TalonNum:string[6];
	QRImMass:array[1..30] of TQRImage;
	QRLabMass:array[1..60] of TQRLabel;
	QRLabDem:array[1..30] of TQRLabel;
	//v_TalType:T_TalonType;
	v_Ini:string;
	v_FlgMirr:Boolean=False;
	v_Sleep:Integer;

function AddZero(n: Cardinal; Count: Integer): string;

implementation

uses RTLConsts;

{$R *.dfm}

function AddZero(n: Cardinal; Count: Integer): string;
begin
	Result:=StringReplace(Format('%'+IntToStr(Count)+'u',[n]),' ','0',[rfReplaceAll]);
end;

procedure TForm1.FormShow(Sender: TObject);
var
	vBuf:string;
begin
	v_Ini:=_ApplPath+'talon.ini';
	vBuf:=_GetIniItem(v_Ini,c_Sec,'lnum');
	v_LastNo:=_IIF(vBuf='',1,StrToInt(vBuf));

	vBuf:=_GetIniItem(v_Ini,c_Sec,'ser');
	edSheets.Text:=_GetIniItem(v_Ini,c_Sec,'ll');
	v_Ser:=_IIF(vBuf='',1,StrToInt(vBuf));

	vBuf:=_GetIniItem(v_Ini,c_Sec,'month');
	v_Month:=_IIF(vBuf='','00',vBuf);
	edMonth.Text:=v_Month;

	StatusBar1.Panels.Items[1].Text:=IntToStr(v_LastNo);
	StatusBar1.Panels.Items[2].Text:=c_UkrString[v_Ser];

	SetMassOfQR;
	edSeries.Text:=Trim(c_UkrString[v_Ser]);
	edFromNum.Text:=IntToStr(v_LastNo+1);
end;

Procedure TForm1.FormClose(Sender: TObject; var Action: TCloseAction);
begin
	//CloseFile(v_File);
end;

procedure TForm1.btnPrintClick(Sender: TObject);
var
	i,k:Integer;
	vLastDigit:byte;
	//vPolyShtT:Byte;
	vStartNum,vNextNum:Integer;
	vPos1,vPos2:Integer;
	vPTop,vPLeft:Extended;
	vVal:string[2];
	vOnly1,vOnly2:Integer;
	vList:TStringList;
	vTalons:array[1..30]of T_TalonId;
	vRow,vCol,vPlace:Integer;
	vMult:Integer;
	vCurRow:Integer;
	//=========================
	function i_GetPlace(aDim:Integer):Integer;
	begin
		if not v_FlgMirr then
			Result:=aDim
		else
		begin
			vRow:=aDim div 6;
			vCol:=aDim mod 6;
			if vCol=0 then
			begin
				vRow:=vRow-1;
				vCol:=1;
			end
			else
			begin
				vCol:=7-vCol;
			end;
			Result:=vRow*6+vCol;
		end;
	end;
	//==========================
begin
	btnPrint.Enabled:=False;

	v_FlgMirr:=chbMirror.Checked;

	if Trim(edFromNum.Text)='' then
		vStartNum:=v_LastNo+1
	else
		vStartNum:=StrToInt(edFromNum.Text);

	k:=1;
	vMult:=1;
	if chbLowerOut.Checked then
	begin
		Inc(vStartNum,StrToInt(edSheets.Text)-1);
		k:=StrToInt(edSheets.Text);
		vMult:=-1
	end;

	v_Ser:=Pos(Trim(edSeries.Text),c_UkrString);
	v_Sleep:=StrToInt(_GetIniItem(v_Ini,c_Sec,'sleep'));

	vPTop:=QuickRep1.Page.TopMargin;
	vPLeft:=QuickRep1.Page.LeftMargin;

	vList:=TStringList.Create;
	try
		vList.CommaText:=_GetIniItem(v_Ini,c_Sec,'t');

		if vList.Count<>TALONS_ON_LIST then
		begin
			_MsgBoxTop(['Print','Количество талонов должно быть равно 30']);
			Abort;
		end;

		// формирование значения талонов на листе
		for i:=1 to TALONS_ON_LIST do
		begin

			vPlace:=i_GetPlace(i);

			vPos1:=Pos('-',vList[vPlace-1]);
			vTalons[i].TalonType:=StrToInt(LeftStr(vList[vPlace-1],vPos1-1));
			case StrToInt(Copy(vList[vPlace-1],vPos1+1,2)) of
				75:
						vTalons[i].ValueType:=0;
				 1:
						vTalons[i].ValueType:=1;
				11:
						vTalons[i].ValueType:=2;
				 5:
						vTalons[i].ValueType:=3;
				 8:
						vTalons[i].ValueType:=4;
				12:
						vTalons[i].ValueType:=5;
				16:
						vTalons[i].ValueType:=6;
			else
				begin
					_MsgBoxTop(['Print','Ошибка в значении объема талона №'+IntToStr(1)]);
					Abort;
				end;
			end;//case
		end;//for
		//\\ формирование значения талонов на листе
	finally
		vList.Free;
	end;

	try
		QuickRep1.Page.TopMargin:=QuickRep1.Page.TopMargin+StrToInt(edFromTop.Text);
		//QuickRep1.Page.LeftMargin:=QuickRep1.Page.LeftMargin+StrToInt(edFromLeft.Text);

		if (chbPart.Checked) and (edPart.Text<>'') and
				((StrToInt(edPart.Text)>0) and (StrToInt(edPart.Text)<=50)) then
		begin
			if edListOnly1.Text='' then //1-я партия
			begin
				if chbLowerOut.Checked then
				begin
					vOnly1:=StrToInt(edSheets.Text)-StrToInt(edPart.Text)+1;
					vOnly2:=StrToInt(edSheets.Text);
				end
				else
				begin
					vOnly1:=1;
					vOnly2:=StrToInt(edPart.Text);
				end;
			end
			else //следующая партия
			begin
				vOnly1:=StrToInt(edListOnly1.Text)+(StrToInt(edPart.Text)*vMult);
				vOnly2:=StrToInt(edListOnly2.Text)+(StrToInt(edPart.Text)*vMult);
			end;
			edListOnly1.Text:=IntToStr(vOnly1);
			edListOnly2.Text:=IntToStr(vOnly2);
		end
		else if (edListOnly1.Text='') and (edListOnly2.Text='') then
		begin
			vOnly1:=1;
			vOnly2:=StrToInt(edSheets.Text);
		end
		else if (edListOnly2.Text='') and (edListOnly1.Text<>'') then
		begin
			vOnly1:=StrToInt(edListOnly1.Text);
			vOnly2:=vOnly1;
		end
		else if (edListOnly2.Text<>'') and (edListOnly1.Text<>'') then
		begin
			vOnly1:=StrToInt(edListOnly1.Text);
			vOnly2:=StrToInt(edListOnly2.Text);
		end;

		//
		repeat
			vNextNum:=vStartNum;

			for i:=1 to TALONS_ON_LIST do
			begin

				vPlace:=i_GetPlace(i);

				vPos1:=v_Ser;
				vPos2:=0;
				v_TalonNum:=AddZero(vNextNum,6);

				v_BarCode:=IntToStr(vTalons[vPlace].TalonType)+
										v_TalonNum+
										AddZero(vPos1,2)+
										AddZero(vPos2,2)+
										IntToStr(vTalons[vPlace].ValueType)+'0';
				vLastDigit:=_GetLastDigit(v_BarCode);
				v_BarCode[13]:=IntToStr(vLastDigit)[1];
		//////////////кодирование/////////////////
				vCurRow:=((i-1) div 6)+1;
				//if Pos(IntToStr(vCurRow),edSkip.Text)<>0 then
				Coding(v_BarCode,vPlace,Pos(IntToStr(vCurRow),edSkip.Text)<>0);//?????????
				Inc(vNextNum,StrToInt(edSheets.Text));
			end;//for

			try // вывод на печать
				QuickRep1.ShowProgress:=ChbShowProgress.Checked;
				if not((k>=vOnly1) and (k<=vOnly2)) then //пропуск печати ненужных номеров
					Continue
				else if chbView.Checked then //печать с предварительным просмотром
					QuickRep1.Preview
				else
				begin
					QuickRep1.Print;
					StatusBar1.Panels.Items[1].Text:=IntToStr(k);//отображение в статус-баре
					Application.ProcessMessages;
				end;
			finally

				// пересчет номеров для следующего листа в зависимости от лотка
				if chbLowerOut.Checked then
				begin
					Dec(vStartNum);
					Dec(k);
				end
				else
				begin
					Inc(vStartNum);
					Inc(k);
				end;
			end;

			Sleep(v_Sleep);

		until (k<1) or (k>StrToInt(edSheets.Text));

	finally
		QuickRep1.Page.TopMargin:=vPTop;
		QuickRep1.Page.LeftMargin:=vPLeft;
	end;

	StatusBar1.Panels.Items[1].Text:='';
	StatusBar1.Panels.Items[2].Text:='';

  if (chbPart.Checked) and
			( ((vMult=1) and (StrToInt(edListOnly2.Text)>=StrToInt(edSheets.Text))) or
				((vMult=-1) and (StrToInt(edListOnly1.Text)<=1)) ) then
	begin
		v_LastNo:=StrToInt(v_TalonNum)+StrToInt(edSheets.Text)-1;
		StatusBar1.Panels.Items[1].Text:=IntToStr(v_LastNo);
		StatusBar1.Panels.Items[2].Text:=c_UkrString[v_Ser];
		_SetIniItem(v_Ini,c_Sec,'lnum',IntToStr(v_LastNo));
		_SetIniItem(v_Ini,c_Sec,'ser',IntToStr(v_Ser));
		_SetIniItem(v_Ini,c_Sec,'ll',edSheets.Text);
		_SetIniItem(v_Ini,c_Sec,'part',edSheets.Text);
		_SetIniItem(v_Ini,c_Sec,'month',v_Month);
		edFromNum.Text:=IntToStr(v_LastNo+1);
		edListOnly1.Clear;
		edListOnly2.Clear;
	end;

	btnPrint.Enabled:=True;
end;

procedure TForm1.DrawCode(aMatrix: string; aItNum: Byte; aInvisible:Boolean=False);
var
	i:Integer;
	vTop:Integer;
	ss:String;
begin
	QRImMass[aItNum].Canvas.Brush.Color:=clWhite;
	QRImMass[aItNum].Canvas.FillRect(Rect(0,0,QRImMass[aItNum].Width,QRImMass[aItNum].Height));
//120515
	if aInvisible then
		Exit;
//\\120515
	QRImMass[aItNum].Canvas.Pen.Color:=clBlack;

	vTop:=1;
	for i:=1 to Length(aMatrix) do
	begin
		if aMatrix[i]='1' then
			QRImMass[aItNum].Canvas.PolyLine([Point(10+i,vTop),Point(10+i,25)])
		else
			if aMatrix[i]='x' then
				QRImMass[aItNum].Canvas.PolyLine([Point(10+i,vTop),Point(10+i,30)]);
	end;

	QRImMass[aItNum].Canvas.Font.Name:='Arial';
	QRImMass[aItNum].Canvas.TextOut(3,25,v_BarCode[1]);
	QRImMass[aItNum].Canvas.TextOut(17,25,copy(v_BarCode,2,6));
	QRImMass[aItNum].Canvas.TextOut(63,25,copy(v_BarCode,8,6));
end;

procedure TForm1.Coding(aNum : string; aItemNumb: Byte; aInvisible:Boolean=False);
var
	vMatrix: string;
	vColor: TColor;
	i: Integer;
begin

	if aInvisible then
		vColor:=clWhite
	else
		vColor:=clBlack;

	vMatrix:='';
	if Length(aNum)=13 then
	begin
		if not aInvisible then
		begin
			vMatrix:=vMatrix+'x0x'; // начало штрих-кода
			vMatrix:=vMatrix+EAN_izqA[StrToInt(aNum[2])];

			for i:=3 to 7 do
			begin
				if CodificaIzq[StrToInt(aNum[1])][i-3]='A' then
					vMatrix:=vMatrix+EAN_izqA[StrToInt(aNum[i])]
				else
					vMatrix:=vMatrix+EAN_izqB[StrToInt(aNum[i])];
			end;

			vMatrix:=vMatrix+'0x0x0'; // центр штрих-кода
			vMatrix:=vMatrix+EAN_dcha[StrToInt(aNum[8])];
			vMatrix:=vMatrix+EAN_dcha[StrToInt(aNum[9])];
			vMatrix:=vMatrix+EAN_dcha[StrToInt(aNum[10])];
			vMatrix:=vMatrix+EAN_dcha[StrToInt(aNum[11])];
			vMatrix:=vMatrix+EAN_dcha[StrToInt(aNum[12])];
			vMatrix:=vMatrix+EAN_dcha[StrToInt(aNum[13])];
			vMatrix:=vMatrix+'x0x'; // конец штрих-кода
		end;
		Form1.DrawCode(vMatrix,aItemNumb,aInvisible);
		QRLabMass[aItemNumb*2-1].Font.Size:=10;
		QRLabMass[aItemNumb*2-1].Font.Color:=vColor;
		QRLabMass[aItemNumb*2-1].Font.Charset:=RUSSIAN_CHARSET;
		QRLabMass[aItemNumb*2-1].Caption:='Серія '+c_UkrString[v_Ser];
		QRLabMass[aItemNumb*2].Font.Size:=10;
		QRLabMass[aItemNumb*2].Font.Color:=vColor;
		QRLabMass[aItemNumb*2].Font.Charset:=RUSSIAN_CHARSET;
		QRLabMass[aItemNumb*2].Caption:='№ '+v_TalonNum;

		QRLabDem[aItemNumb].Font.Size:=6;
		QRLabDem[aItemNumb].Font.Color:=vColor;
		QRLabDem[aItemNumb].Font.Charset:=RUSSIAN_CHARSET;
		QRLabDem[aItemNumb].Caption:=v_Month;

	end;
end;

procedure TForm1.SetMassOfQR;
begin
	QRImMass[1]:=QRImage1;
	QRImMass[2]:=QRImage2;
	QRImMass[3]:=QRImage3;
	QRImMass[4]:=QRImage4;
	QRImMass[5]:=QRImage5;
	QRImMass[6]:=QRImage6;
	QRImMass[7]:=QRImage7;
	QRImMass[8]:=QRImage8;
	QRImMass[9]:=QRImage9;
	QRImMass[10]:=QRImage10;
	QRImMass[11]:=QRImage11;
	QRImMass[12]:=QRImage12;
	QRImMass[13]:=QRImage13;
	QRImMass[14]:=QRImage14;
	QRImMass[15]:=QRImage15;
	QRImMass[16]:=QRImage16;
	QRImMass[17]:=QRImage17;
	QRImMass[18]:=QRImage18;
	QRImMass[19]:=QRImage19;
	QRImMass[20]:=QRImage20;
	QRImMass[21]:=QRImage21;
	QRImMass[22]:=QRImage22;
	QRImMass[23]:=QRImage23;
	QRImMass[24]:=QRImage24;
	QRImMass[25]:=QRImage25;
	QRImMass[26]:=QRImage26;
	QRImMass[27]:=QRImage27;
	QRImMass[28]:=QRImage28;
	QRImMass[29]:=QRImage29;
	QRImMass[30]:=QRImage30;

	QRLabMass[1]:=QRLabel1;
	QRLabMass[2]:=QRLabel2;
	QRLabMass[3]:=QRLabel3;
	QRLabMass[4]:=QRLabel4;
	QRLabMass[5]:=QRLabel5;
	QRLabMass[6]:=QRLabel6;
	QRLabMass[7]:=QRLabel7;
	QRLabMass[8]:=QRLabel8;
	QRLabMass[9]:=QRLabel9;
	QRLabMass[10]:=QRLabel10;
	QRLabMass[11]:=QRLabel11;
	QRLabMass[12]:=QRLabel12;
	QRLabMass[13]:=QRLabel13;
	QRLabMass[14]:=QRLabel14;
	QRLabMass[15]:=QRLabel15;
	QRLabMass[16]:=QRLabel16;
	QRLabMass[17]:=QRLabel17;
	QRLabMass[18]:=QRLabel18;
	QRLabMass[19]:=QRLabel19;
	QRLabMass[20]:=QRLabel20;
	QRLabMass[21]:=QRLabel21;
	QRLabMass[22]:=QRLabel22;
	QRLabMass[23]:=QRLabel23;
	QRLabMass[24]:=QRLabel24;
	QRLabMass[25]:=QRLabel25;
	QRLabMass[26]:=QRLabel26;
	QRLabMass[27]:=QRLabel27;
	QRLabMass[28]:=QRLabel28;
	QRLabMass[29]:=QRLabel29;
	QRLabMass[30]:=QRLabel30;
	QRLabMass[31]:=QRLabel31;
	QRLabMass[32]:=QRLabel32;
	QRLabMass[33]:=QRLabel33;
	QRLabMass[34]:=QRLabel34;
	QRLabMass[35]:=QRLabel35;
	QRLabMass[36]:=QRLabel36;
	QRLabMass[37]:=QRLabel37;
	QRLabMass[38]:=QRLabel38;
	QRLabMass[39]:=QRLabel39;
	QRLabMass[40]:=QRLabel40;
	QRLabMass[41]:=QRLabel41;
	QRLabMass[42]:=QRLabel42;
	QRLabMass[43]:=QRLabel43;
	QRLabMass[44]:=QRLabel44;
	QRLabMass[45]:=QRLabel45;
	QRLabMass[46]:=QRLabel46;
	QRLabMass[47]:=QRLabel47;
	QRLabMass[48]:=QRLabel48;
	QRLabMass[49]:=QRLabel49;
	QRLabMass[50]:=QRLabel50;
	QRLabMass[51]:=QRLabel51;
	QRLabMass[52]:=QRLabel52;
	QRLabMass[53]:=QRLabel53;
	QRLabMass[54]:=QRLabel54;
	QRLabMass[55]:=QRLabel55;
	QRLabMass[56]:=QRLabel56;
	QRLabMass[57]:=QRLabel57;
	QRLabMass[58]:=QRLabel58;
	QRLabMass[59]:=QRLabel59;
	QRLabMass[60]:=QRLabel60;

	QRLabDem[1]:=QRL1;
	QRLabDem[2]:=QRL2;
	QRLabDem[3]:=QRL3;
	QRLabDem[4]:=QRL4;
	QRLabDem[5]:=QRL5;
	QRLabDem[6]:=QRL6;
	QRLabDem[7]:=QRL7;
	QRLabDem[8]:=QRL8;
	QRLabDem[9]:=QRL9;
	QRLabDem[10]:=QRL10;
	QRLabDem[11]:=QRL11;
	QRLabDem[12]:=QRL12;
	QRLabDem[13]:=QRL13;
	QRLabDem[14]:=QRL14;
	QRLabDem[15]:=QRL15;
	QRLabDem[16]:=QRL16;
	QRLabDem[17]:=QRL17;
	QRLabDem[18]:=QRL18;
	QRLabDem[19]:=QRL19;
	QRLabDem[20]:=QRL20;
	QRLabDem[21]:=QRL21;
	QRLabDem[22]:=QRL22;
	QRLabDem[23]:=QRL23;
	QRLabDem[24]:=QRL24;
	QRLabDem[25]:=QRL25;
	QRLabDem[26]:=QRL26;
	QRLabDem[27]:=QRL27;
	QRLabDem[28]:=QRL28;
	QRLabDem[29]:=QRL29;
	QRLabDem[30]:=QRL30;
end;

procedure TForm1.mmiPrinterClick(Sender: TObject);
begin
	QuickRep1.PrinterSetup;
end;

procedure TForm1.mmExitClick(Sender: TObject);
begin
	Application.Terminate;
end;

procedure TForm1.FormClick(Sender: TObject);
begin
	Form1.Update;
end;

procedure TForm1.edSheetsChange(Sender: TObject);
var
	vNum:Integer;
begin
	try
		vNum:=StrToInt(edSheets.Text);
		if vNum=0 then
			edSheets.Text:='0';
	except
		ShowMessage('Вводите только цифры');
		edSheets.Text:='0';
	end;
end;

procedure TForm1.cmbTypeChange(Sender: TObject);
begin
	//StatusBar1.Panels.Items[3].Text:=cmbType.Text;
end;

procedure TForm1.btnFromNumClearClick(Sender: TObject);
begin
	try
		edFromNum.Clear;
	except
	end;
end;

procedure TForm1.btnListOnlyClearClick(Sender: TObject);
begin
	edListOnly1.Clear;
	edListOnly2.Clear;
end;

procedure TForm1.chbMirrorClick(Sender: TObject);
begin
	v_FlgMirr:=chbMirror.Checked
end;

procedure TForm1.btnPartClearClick(Sender: TObject);
begin
	edPart.Clear;
end;

procedure TForm1.btnSkipClearClick(Sender: TObject);
begin
	edSkip.Clear;
end;

end.
