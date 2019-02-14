import random
import turtle

#Setup
w = turtle.Screen()
w.title("wallpaper")
w.bgcolor("black")
w.setup(width=1980, height=1080)
w.tracer(0)

#Fonts
list = ['Al Bayan', 'Al Nile', 'Al Tarikh', 'American Typewriter', 'Andale Mono', 'Arial', 'Arial Black', 'Arial Hebrew', 'Arial Hebrew Scholar', 'Arial Narrow', 'Arial Rounded MT Bold', 'Arial Unicode MS', 'Athelas', 'Ave Fedan PERSONAL USE ONLY', 'Avenir', 'Avenir Next', 'Avenir Next Condensed', 'Ayuthaya', 'Baghdad', 'Bangla MN', 'Bangla Sangam MN', 'Baoli SC', 'Baoli TC', 'Baskerville', 'Beirut', 'BiauKai', 'Big Caslon', 'Birch Std', 'Bit5x3', 'Blackoak Std', 'Bodoni 72', 'Bodoni 72 Oldstyle', 'Bodoni 72 Smallcaps', 'Bodoni Ornaments', 'Bradley Hand', 'Brush Script MT', 'Brush Script Std', 'Chalkboard', 'Chalkboard SE', 'Chalkduster', 'Chaparral Pro', 'Charlemagne Std', 'Charter', 'Cochin', 'Comic Sans MS', 'Copperplate', 'Corsiva Hebrew', 'Courier', 'Courier New', 'Damascus', 'DecoType Naskh', 'Devanagari MT', 'Devanagari Sangam MN', 'Didot', 'DIN Alternate', 'DIN Condensed', 'Diwan Kufi', 'Diwan Thuluth', 'Euphemia UCAS', 'Farah', 'Farisi', 'Futura', 'GB18030 Bitmap', 'Geeza Pro', 'Geneva', 'Georgia', 'Gill Sans', 'Gujarati MT', 'Gujarati Sangam MN', 'GungSeo', 'Gurmukhi MN', 'Gurmukhi MT', 'Gurmukhi Sangam MN', 'Hannotate SC', 'Hannotate TC', 'HanziPen SC', 'HanziPen TC', 'HeadLineA', 'Hei', 'Heiti SC', 'Heiti TC', 'Helvetica', 'Helvetica Neue', 'Herculanum', 'Hiragino Kaku Gothic Pro', 'Hiragino Kaku Gothic ProN', 'Hiragino Kaku Gothic Std', 'Hiragino Kaku Gothic StdN', 'Hiragino Maru Gothic Pro', 'Hiragino Maru Gothic ProN', 'Hiragino Mincho Pro', 'Hiragino Mincho ProN', 'Hiragino Sans', 'Hiragino Sans CNS', 'Hiragino Sans GB', 'Hobo Std', 'Hoefler Text', 'Impact', 'InaiMathi', 'Iowan Old Style', 'ITF Devanagari', 'ITF Devanagari Marathi', 'Kai', 'Kailasa', 'Kaiti SC', 'Kaiti TC', 'Kannada MN', 'Kannada Sangam MN', 'Kefa', 'Khmer MN', 'Khmer Sangam MN', 'Klee', 'Kohinoor Bangla', 'Kohinoor Devanagari', 'Kohinoor Telugu', 'Kokonor', 'Kozuka Gothic Pr6N', 'Kozuka Gothic Pro', 'Kozuka Mincho Pr6N', 'Kozuka Mincho Pro', 'Krungthep', 'KufiStandardGK', 'Lantinghei SC', 'Lantinghei TC', 'Lao MN', 'Lao Sangam MN', 'Letter Gothic Std', 'Libian SC', 'Libian TC', 'LiHei Pro', 'LingWai SC', 'LingWai TC', 'LiSong Pro', 'Lithos Pro', 'Lucida Grande', 'Luminari', 'Malayalam MN', 'Malayalam Sangam MN', 'Marion', 'Marker Felt', 'Menlo', 'Microsoft Sans Serif', 'Minion Pro', 'Mishafi', 'Mishafi Gold', 'Monaco', 'Mshtakan', 'Muna', 'Myanmar MN', 'Myanmar Sangam MN', 'Myriad Arabic', 'Myriad Hebrew', 'Myriad Pro', 'Nadeem', 'Nanum Brush Script', 'Nanum Gothic', 'Nanum Myeongjo', 'Nanum Pen Script', 'New Peninim MT', 'Noteworthy', 'Noto Nastaliq Urdu', 'Nueva Std', 'OCR A Std', 'Optima', 'Orator Std', 'Oriya MN', 'Oriya Sangam MN', 'Osaka', 'Palatino', 'Papyrus', 'PCMyungjo', 'Phosphate', 'PilGi', 'PingFang HK', 'PingFang SC', 'PingFang TC', 'Plantagenet Cherokee', 'Poplar Std', 'Prestige Elite Std', 'PT Mono', 'PT Sans', 'PT Sans Caption', 'PT Sans Narrow', 'PT Serif', 'PT Serif Caption', 'Raanana', 'Rockwell', 'Sana', 'Sathu', 'Savoye LET', 'Seravek', 'Shree Devanagari 714', 'SignPainter', 'Silom', 'Sinhala MN', 'Sinhala Sangam MN', 'Skia', 'Snell Roundhand', 'Songti SC', 'Songti TC', 'Source Sans Pro', 'STFangsong', 'STHeiti', 'STIXGeneral', 'STIXIntegralsD', 'STIXIntegralsSm', 'STIXIntegralsUp', 'STIXIntegralsUpD', 'STIXIntegralsUpSm', 'STIXNonUnicode', 'STIXSizeFiveSym', 'STIXSizeFourSym', 'STIXSizeOneSym', 'STIXSizeThreeSym', 'STIXSizeTwoSym', 'STIXVariants', 'STKaiti', 'STSong', 'Sukhumvit Set', 'Superclarendon', 'Symbol', 'Tahoma', 'Tamil MN', 'Tamil Sangam MN', 'Tekton Pro', 'Telugu MN', 'Telugu Sangam MN', 'Thonburi', 'Times', 'Times New Roman', 'Toppan Bunkyu Gothic', 'Toppan Bunkyu Midashi Gothic', 'Toppan Bunkyu Midashi Mincho', 'Toppan Bunkyu Mincho', 'Trajan Pro 3', 'Trattatello', 'Trebuchet MS', 'Tsukushi A Round Gothic', 'Tsukushi B Round Gothic', 'Verdana', 'Waseem', 'Wawati SC', 'Wawati TC', 'Webdings', 'Weibei SC', 'Weibei TC', 'Wingdings', 'Wingdings 2', 'Wingdings 3', 'Xingkai SC', 'Xingkai TC', 'Yuanti SC', 'Yuanti TC', 'YuGothic', 'YuKyokasho', 'YuKyokasho Yoko', 'YuMincho', 'YuMincho +36p Kana', 'Yuppy SC', 'Yuppy TC', 'Zapf Dingbats', 'Zapfino', 'Adobe Arabic', 'Adobe Caslon Pro', 'Adobe Devanagari', 'Adobe Fan Heiti Std', 'Adobe Fangsong Std', 'Adobe Garamond Pro', 'Adobe Gothic Std', 'Adobe Gurmukhi', 'Adobe Hebrew', 'Adobe Heiti Std', 'Adobe Kaiti Std', 'Adobe Ming Std', 'Adobe Myungjo Std', 'Adobe Naskh', 'Adobe Song Std', 'Apple Braille', 'Apple Chancery', 'Apple Color Emoji', 'Apple LiGothic', 'Apple LiSung', 'Apple SD Gothic Neo', 'Apple Symbols', 'AppleGothic', 'AppleMyungjo']


def showWord(message, a):
    for i in range(1,a):
        word_i = turtle.Turtle()
        word_i.speed(0)
#colors
        number_of_colors = 20
        color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(number_of_colors)]
        word_i.color(random.choice(color))

        word_i.penup()
        word_i.hideturtle()
#Coords
        x = random.randrange(-990, 990)
        y = random.randrange(-540, 540)
        word_i.goto(x, y)
#Font
        font = random.choice(list)
        size = random.randrange(5, 100)
        word_i.write(message, align="center", font=(font, size, "normal"))
        i += i

#Main
showWord("Python", 50)
w.update()
w.mainloop()
