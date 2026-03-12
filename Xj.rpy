#Xeti's Korean utility plugins
init python:
    def j(word, particle):
        if word is None:
            return ""
            
        target_word = renpy.translate_string(word)

        if not target_word:
            return ""

        last_char = target_word[-1]
        code = ord(last_char)

        has_batchim = False
        if 0xAC00 <= code <= 0xD7A3:
            has_batchim = (code - 0xAC00) % 28 != 0
        
        mapping = {
            '은': ('은', '는'),
            '는': ('은', '는'),
            '이': ('이', '가'),
            '가': ('이', '가'),
            '을': ('을', '를'),
            '를': ('을', '를'),
            '과': ('과', '와'),
            '와': ('과', '와'),
            '아': ('아', '야'),
            '야': ('아', '야'),
            '이여': ('이여', '여'),
            '여': ('이여', '여'),
            '이랑': ('이랑', '랑'),
            '랑': ('이랑', '랑'),
            '이나': ('이나', '나'),
            '나': ('이나', '나'),
            '이란': ('이란', '란'),
            '란': ('이란', '란'),
            '이며': ('이며', '며'),
            '며': ('이며', '며'),
            '이라는': ('이라는', '라는'),
            '라는': ('이라는', '라는'),
            '이라고': ('이라고', '라고'),
            '라고': ('이라고', '라고'),
            '이라면': ('이라면', '라면'),
            '라면': ('이라면', '라면'),
            '이에요': ('이에요', '예요'),
            '예요': ('이에요', '예요'),
        }

        if particle in mapping:
            josa_o, josa_x = mapping[particle]
            selected_josa = josa_o if has_batchim else josa_x
            return target_word + selected_josa
        else:
            return target_word + particle
