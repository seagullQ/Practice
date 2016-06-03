# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .. import Provider as LoremProvider


class Provider(LoremProvider):
    word_list = (
            "夕颜","秋恋","蝉羽","浴兰","沉鱼","落雁","闭月","羞花","幽然","静微",
            "艺雅","卉馨","轩然","子茹","萦绕","流萤","静谧","流凨","羽翼","蔓延",
            "浅唱","轻盈","清芳","黯淡","纯洁","涤荡","皓月","思琪","绚烂","郁葱",
            "寂寞","尘世","词语","疼痛","猜测","奔腾","丑陋","长久","模仿","固定",
            "寒冷","恐惧","奇怪","整齐","漂浮","特殊","虚假","遥望","微弱","消灭",
            "珍贵","祝愿","缠绕","颤抖","抚摩","拉扯","柔软","明亮","宽敞","黑暗",
            "破旧","美好","飞翔","挖掘","搜索","期待","盼望","祈祷","微小","捕捉",
            "思忖","思量","思想","思念","思绪","思索","思维","思考","思辨","思路",
            "思慕","思逸","思齐","思远","思春","思韵","思虑","思辩","思玄","思恋",
            "思凡","思致","思惟","思潮","思忆","思元","思绎","思域","思永","思怀",
            "思越","思纬","思理","思莼","思服","思咏","思愆","思议","思秋","思言",
            "馨香","飘散","舒展","娇美","神韵","恬静","醉人","素雅","娇嫩","幽香",
            "淡雅","朴素","花瓣","花蕊","花粉","鲜花","怒放","含苞","孤单","孤寂寂寞",
            "寥寂","寂寥","落寞","孤独","寂静","僻静","宁静","寂然","清静","沉寂",
            "沉静","安静","孤立","伶仃","孤单","零落","落莫","动静","呼吸","朝夕",
            "取舍","善恶","兴衰","祸福","甘苦","彼此","首尾","褒贬","吞吐","黑白",
            "是非","多少","真假","虚实","反正","生死","悲欢","前后","始末","早晚",
            "昼夜","曲直","东西","善恶","南北","开关","左右","眷恋","留恋","依恋",
            "迷恋","自恋","爱恋","失恋","贪恋","思恋","热恋","怀恋","初恋","顾恋",
            "流恋","恋恋","悲恋","相恋","婉恋","忆恋","积恋","恳恋","情恋","凝恋",
            "耽恋","欣恋","绻恋","感恋","单恋","遐恋","嫪恋","安恋","慕恋","兴奋",
            "快乐","喜悦","愉快","畅快","欢畅","欢喜","欢腾","欢快","欣喜","激奋",
            "激昂","激情","敬佩","佩服","崇拜","钦仰","惊恐","惊慌","惊吓","惧怕",
            "恐惧","胆怯","畏缩","发慌","心慌","恐慌","激怒","恼火","怒斥","怒吼",
            "震怒","气愤","担忧","发愁","犯愁","忧伤","忧愁","忧心","愁闷","悲伤",
            "悲痛","悲惨","悲凉","哀伤","哀怨","忧伤","伤感","瘦削","憔悴","俊美",
            "恬静","慈祥","苍白","白皙","清秀","光滑","英俊","红润","挺直","扁平",
            "小巧","笔直","端庄","秀气","秀美","巧嘴","朱唇","苍白","红润","干裂",
            "娇嫩","整齐","整洁","雪白","焦黄","洁净","蓬松","鲜嫩","粉红","通红",
            "红嫩","滑润","滋润","干巴","干裂","干燥","蜡黄","洁白","炭黑","瘦弱",
            "矮小","苗条","丰满","强壮","清秀","单薄","文弱","干瘦","轩昂","文辞",
            "短语","单词","词组","词汇","字眼","范例","语素","丰富","信息","组成",
            "最小","最大","造句","单位","构成","方式","可以","神奇","单纯","自由",
            "单音","双音","多音","可以","山高","水深","天高","地厚","拥有","凑整",
            "仿佛","苍茫","参差","上面","前方","内部","中间","方位","名词","学生",
            "老师","群众","老头","妇女","同志","叔叔","婶婶","爸爸","妈妈","哥哥",
            "弟弟","姐姐","妹妹","事物","蜗牛","猎豹","棒球","足球","蓝求","战机",
            "飞机","地球","思想","中学","物理","科穴","碗盘","竹筷","上午","下午",
            "过去","将来","早晨","午夜","三更","甲戊","世纪","今天","昨天","动词",
            "行为","跑步","唱歌","喝水","敲门","吆喝","踢求","生长","枯萎","发芽",
            "结果","产卵","喜欢","气愤","觉得","思考","厌恶","存现","消失","显现",
            "丢失","幻灭","使令","使人","让座","命令","禁止","勒令","能愿","如会",
            "愿意","能够","宁可","表示","状貌","特征","状态","气急","怒火","高兴",
            "形容","高大","高瘦","矮胖","粗细","强壮","性质","香甜","漂亮","圆滑",
            "机智","单调","快速","浓厚","肥满","许多","迅速","悄悄","量词","单位",
            "公尺","分寸","公里","公斤","一两","一辆","一角","一元","一次","一趟",
            "一下","回声","一幢","一座","代词","代替","我们","你们","它们","她们",
            "大家","咱们","疑问","谁的","什么","怎么","哪里","何以","这里","那里",
            "那边","拟声","模拟","声音","轰隆","淅沥","噼里","啪啦","哗啦","叽喳",
            "啪拉","哄堂","开怀","笑颜","笑容","喜笑","欢声","笑语","眉开","生气",
            "火冒","雷霆","欣喜","心情","词汇","忧愁","丧气","雾气","满腹","满腔",
            "愁肠","百结","欲断","寸断","九转","百愁","心事","阴郁","忧心","如焚",
            "愁绪")
    
    crops_list={'水稻','豆类','薯类','青稞','蚕豆','小麦','油籽','蔓青','大芥','胡麻','大麻',
                '向日葵','萝卜','白菜','芹菜','韭菜','蒜','葱','胡萝卜','菜瓜','莲花菜','菊芋',
                '刀豆','芫荽','莴笋','黄花','辣椒','黄瓜','西红柿','梨','苹果','桃','杏','核桃',
                '李子','樱桃','草莓','林檎','酸梨','野杏','毛桃','苞瑙','山樱桃','沙棘','草莓',
                '玉米','绿肥','紫云英','烟草','咖啡','人参','当归','金银花'}
    @classmethod
    def crops(cls):
        """
        Generate a random crops
        :example '草莓'
        """
        return cls.random_element(cls.crops_list)
    
    @classmethod
    def word(cls):
        """
        Generate a random word
        :example 'lorem'
        """
        return cls.random_element(cls.word_list)

    @classmethod
    def words(cls, nb=3):
        """
        Generate an array of random words
        :example array('Lorem', 'ipsum', 'dolor')
        :param nb how many words to return
        """
        return [cls.word() for _ in range(0, nb)]

    @classmethod
    def sentence(cls, nb_words=6, variable_nb_words=True):
        """
        Generate a random sentence
        :example 'Lorem ipsum dolor sit amet.'
        :param nb_words around how many words the sentence should contain
        :param variable_nb_words set to false if you want exactly $nbWords returned,
            otherwise $nbWords may vary by +/-40% with a minimum of 1
        """
        if nb_words <= 0:
            return ''

        if variable_nb_words:
            nb_words = cls.randomize_nb_elements(nb_words)

        words = cls.words(nb_words)
        words[0] = words[0].title()

        return "".join(words)

    @classmethod
    def sentences(cls, nb=3):
        """
        Generate an array of sentences
        :example array('Lorem ipsum dolor sit amet.', 'Consectetur adipisicing eli.')
        :param nb how many sentences to return
        :return list
        """
        return [cls.sentence() for _ in range(0, nb)]

    @classmethod
    def paragraph(cls, nb_sentences=3, variable_nb_sentences=True):
        """
        Generate a single paragraph
        :example 'Sapiente sunt omnis. Ut pariatur ad autem ducimus et. Voluptas rem voluptas sint modi dolorem amet.'
        :param nb_sentences around how many sentences the paragraph should contain
        :param variable_nb_sentences set to false if you want exactly $nbSentences returned,
            otherwise $nbSentences may vary by +/-40% with a minimum of 1
        :return string
        """
        if nb_sentences <= 0:
            return ''

        if variable_nb_sentences:
            nb_sentences = cls.randomize_nb_elements(nb_sentences)

        return "，".join(cls.sentences(nb_sentences))+"。"

    @classmethod
    def paragraphs(cls, nb=3):
        """
        Generate an array of paragraphs
        :example array($paragraph1, $paragraph2, $paragraph3)
        :param nb how many paragraphs to return
        :return array
        """
        return [cls.paragraph() for _ in range(0, nb)]

    @classmethod
    def text(cls, max_nb_chars=200):
        """
        Generate a text string.
        Depending on the $maxNbChars, returns a string made of words, sentences, or paragraphs.
        :example 'Sapiente sunt omnis. Ut pariatur ad autem ducimus et. Voluptas rem voluptas sint modi dolorem amet.'
        :param max_nb_chars Maximum number of characters the text should contain (minimum 5)
        :return string
        """
        text = []
        if max_nb_chars < 5:
            raise ValueError('text() can only generate text of at least 5 characters')

        if max_nb_chars < 25:
            # join words
            while not text:
                size = 0
                # determine how many words are needed to reach the $max_nb_chars once;
                while size < max_nb_chars:
                    word = (' ' if size else '') + cls.word()
                    text.append(word)
                    size += len(word)
                text.pop()
            text[0] = text[0][0].upper() + text[0][1:]
            last_index = len(text) - 1
            text[last_index] += '.'
        elif max_nb_chars < 100:
            # join sentences
            while not text:
                size = 0
                # determine how many sentences are needed to reach the $max_nb_chars once
                while size < max_nb_chars:
                    sentence = (' ' if size else '') + cls.sentence()
                    text.append(sentence)
                    size += len(sentence)
                text.pop()
        else:
            # join paragraphs
            while not text:
                size = 0
                # determine how many paragraphs are needed to reach the $max_nb_chars once
                while size < max_nb_chars:
                    paragraph = ('\n' if size else '') + cls.paragraph()
                    text.append(paragraph)
                    size += len(paragraph)
                text.pop()

        return "".join(text)
