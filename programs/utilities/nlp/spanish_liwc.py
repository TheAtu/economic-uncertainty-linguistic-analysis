from ..python.check_package_availability import check_package_availability

PACKAGES_REQUIERED = ['os','codecs','sys']
LIWCDIC_FILE_DIR = '../data/99-auxiliar/Spanish_LIWC2007_Dictionary.dic'


class liwc:

  def load_liwc_dict(self, liwcdic_file):
      import codecs
      file_content = codecs.open(liwcdic_file, "r", "utf-8").read()
      cate_text = file_content[file_content.find("%")+1:file_content[1:].find("%")].strip()
      for line in cate_text.split("\n"):
          self.liwc_cate_name_by_number[int(line.strip().split("\t")[0])] = line.strip().split("\t")[1]

      dict_text = file_content[file_content[1:].find("%")+2:].strip()
      for line in dict_text.split("\n"):
          self.liwc_cate_number_by_word[line.strip().split("\t")[0]] = set([int(item) for item in line.strip().split("\t")[1:]])

  def __init__(self, liwcdic_file=LIWCDIC_FILE_DIR):
      check_package_availability(PACKAGES_REQUIERED)
      import os
      import sys

      self.liwc_category_names = ["WC",'Funct', 'TotPron', 'PronPer', 'Yo', 'Nosotro', 'TuUtd', 'ElElla', 'Ellos', 'PronImp', 'Articulo', 'Verbos', 'VerbAux', 'Pasado', 'Present', 'Futuro', 'Adverb', 'Prepos', 'Conjunc', 'Negacio', 'Cuantif', 'Numeros', 'Maldec', 'verbYO', 'verbTU', 'verbNOS', 'verbosEL', 'verbELLOS', 'Subjuntiv', 'VosUtds', 'formal', 'informal', 'verbVos', 'Social', 'Familia', 'Amigos', 'Humanos', 'Afect', 'EmoPos', 'EmoNeg', 'Ansiedad', 'Enfado', 'Triste', 'MecCog', 'Insight', 'Causa', 'Discrep', 'Tentat', 'Certeza', 'Inhib', 'Incl', 'Excl', 'Percept', 'Ver', 'Oir', 'Sentir', 'Biolog', 'Cuerpo', 'Salud', 'Sexual', 'Ingerir', 'Relativ', 'Movim', 'Espacio', 'Tiempo', 'Trabajo', 'Logro', 'Placer', 'Hogar', 'Dinero', 'Relig', 'Muerte', 'Asentir', 'NoFluen', 'Relleno']
      self.liwc_cate_name_by_number = {}
      self.liwc_cate_number_by_word = {}

      if os.path.exists(liwcdic_file) == False:
          sys.exit()
      else:
          self.load_liwc_dict(liwcdic_file)

  def getLIWCCount(self, text):
      count_by_categories = {"WC":0,'Funct': 0, 'TotPron': 0, 'PronPer': 0, 'Yo': 0, 'Nosotro': 0, 'TuUtd': 0, 'ElElla': 0, 'Ellos': 0, 'PronImp': 0, 'Articulo': 0, 'Verbos': 0, 'VerbAux': 0, 'Pasado': 0, 'Present': 0, 'Futuro': 0, 'Adverb': 0, 'Prepos': 0, 'Conjunc': 0, 'Negacio': 0, 'Cuantif': 0, 'Numeros': 0, 'Maldec': 0, 'verbYO': 0, 'verbTU': 0, 'verbNOS': 0, 'verbosEL': 0, 'verbELLOS': 0, 'Subjuntiv': 0, 'VosUtds': 0, 'formal': 0, 'informal': 0, 'verbVos': 0, 'Social': 0, 'Familia': 0, 'Amigos': 0, 'Humanos': 0, 'Afect': 0, 'EmoPos': 0, 'EmoNeg': 0, 'Ansiedad': 0, 'Enfado': 0, 'Triste': 0, 'MecCog': 0, 'Insight': 0, 'Causa': 0, 'Discrep': 0, 'Tentat': 0, 'Certeza': 0, 'Inhib': 0, 'Incl': 0, 'Excl': 0, 'Percept': 0, 'Ver': 0, 'Oir': 0, 'Sentir': 0, 'Biolog': 0, 'Cuerpo': 0, 'Salud': 0, 'Sexual': 0, 'Ingerir': 0, 'Relativ': 0, 'Movim': 0, 'Espacio': 0, 'Tiempo': 0, 'Trabajo': 0, 'Logro': 0, 'Placer': 0, 'Hogar': 0, 'Dinero': 0, 'Relig': 0, 'Muerte': 0, 'Asentir': 0, 'NoFluen': 0, 'Relleno': 0}

      count_by_categories["WC"] = len(text.split())

      for word in text.split():

          cate_numbers_word_belongs = set([])
          if word in self.liwc_cate_number_by_word:
              cate_numbers_word_belongs = self.liwc_cate_number_by_word[word]

          else:

              #liwc words have *. eg: balcon*
              word = word[:-1]
              while len(word) > 0:
                  if (word+"*") in self.liwc_cate_number_by_word:
                      cate_numbers_word_belongs = self.liwc_cate_number_by_word[word+"*"]
                      break
                  else:
                      word = word[:-1]

          for num in cate_numbers_word_belongs:
              count_by_categories[self.liwc_cate_name_by_number[num]] += 1

      return count_by_categories