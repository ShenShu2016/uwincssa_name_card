from PIL import Image, ImageDraw, ImageFont
import pandas as pd


df=pd.read_csv("cssa_members_info.csv")

df = df.fillna(' ')
# print(df)
def pil_function(row):
    try:
        sourceFileName = 'qr_code_ChineseName/'+str(row['chinese_name'])+'.jpg'
        # print(sourceFileName)
        qrcode= Image.open(sourceFileName)
        # print (qrcode.format, qrcode.size, qrcode.mode)
        qrcode_resize = qrcode.resize((150, 150),Image.ANTIALIAS)
        # print (qrcode_resize.format, qrcode_resize.size, qrcode_resize.mode)
        background = Image.open("basic_pic/background.jpg")
        bg_size=background.size
        bg_size
        name_english = str(row['english_name'])
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype(r'font/Swiss 721 Bold BT.ttf',55)
        draw.text((100, 140),name_english , fill='#404040', font=font )


        title = str(row['title'])
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype(r'font/Swiss 721 Bold BT.ttf',30)
        draw.text((100, 215),title , fill='#404040', font=font )

        UWCSSA="""UWCSSA"""
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype(r'font/Swiss 721 Bold BT.ttf',55)
        text_width = font.getsize(UWCSSA)
        text_coordinate = int((bg_size[0]-text_width[0])/2), 900
        draw.text(text_coordinate, UWCSSA,fill='#404040', font=font,)

        slash="""-"""
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype(r'font/times.ttf',80)
        text_width = font.getsize(slash)
        text_coordinate = int((bg_size[0]-text_width[0])/2), 930
        draw.text(text_coordinate, slash,(0,0,0), font=font)

        title=str(row['title'])
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype(r'font/arial.ttf',40)
        text_width = font.getsize(title)
        text_coordinate = int((bg_size[0]-text_width[0])/2), 1000
        draw.text(text_coordinate, title,fill='#404040', font=font)

        major=str(row['major'])
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype(r'font/arial.ttf',30)
        draw.text((100, 300),major , fill='#383838', font=font )

        direction=str(row['direction'])
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype(r'font/arial.ttf',30)
        draw.text((100, 340),direction , fill='#383838', font=font )

        telephone=str(row['tele'])
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype(r'font/arial.ttf',30)
        draw.text((100, 420),telephone , fill='#383838', font=font )

        email=str(row['email'])
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype(r'font/arial.ttf',30)
        draw.text((100, 455),email , fill='#383838', font=font )

        university='''University of Windsor'''
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype(r'font/arial.ttf',30)
        draw.text((100, 490),university , fill='#383838', font=font )

        uni_address='''401 Sunset Ave, Windsor, ON N9B 3P4'''
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype(r'font/arial.ttf',30)
        draw.text((100, 525),uni_address , fill='#383838', font=font )

        background.paste(qrcode_resize ,(775,400))

        sourceFileName = "basic_pic/bandge.jpg"
        bandge= Image.open(sourceFileName)
        # print (bandge.format, bandge.size, bandge.mode)
        bandge_resize = bandge.resize((200, 200),Image.ANTIALIAS)
        # print (bandge_resize.format, bandge_resize.size, bandge_resize.mode)
        background.paste(bandge_resize ,(750,100))
        file_name='name_card_EnglishName/'+str(row['english_name'])+'.jpg'
        background.save(file_name)
        print(f"{file_name} success")
    except Exception as e:
        print(e)
        print('fail')



df.apply(pil_function,axis=1,args=())


