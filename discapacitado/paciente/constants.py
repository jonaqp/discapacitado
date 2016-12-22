CODE_CONDITION_NUEVO = '01'
CODE_CONDITION_CONTINUADOR = '02'
STRING_CONDITION_NUEVO = (CODE_CONDITION_NUEVO, 'Nuevo')
STRING_CONDITION_CONTINUADOR = (CODE_CONDITION_CONTINUADOR, 'Continuador')
SIS_CONDITION_LIST = (
    STRING_CONDITION_NUEVO, STRING_CONDITION_CONTINUADOR
)

CODE_TYPE_DOC_NULO = '00'
CODE_TYPE_DOC_DNI = '01'
CODE_TYPE_DOC_CE = '02'
CODE_TYPE_DOC_PAS = '03'
CODE_TYPE_DOC_DIE = '04'
STRING_TYPE_DOC_NULO = (CODE_TYPE_DOC_NULO, 'No Tiene')
STRING_TYPE_DOC_DNI = (CODE_TYPE_DOC_DNI, 'DNI')
STRING_TYPE_DOC_CE = (CODE_TYPE_DOC_CE, 'Carne Extranjeria')
STRING_TYPE_DOC_PAS = (CODE_TYPE_DOC_PAS, 'Pasaporte')
STRING_TYPE_DOC_DIE = (CODE_TYPE_DOC_DIE, 'Documento Identidad Extranjero')
SIS_TYPE_DOC_LIST = (
    STRING_TYPE_DOC_NULO, STRING_TYPE_DOC_DNI, STRING_TYPE_DOC_CE,
    STRING_TYPE_DOC_DIE
)

CODE_FINANCIADOR_NULO = '00'
CODE_FINANCIADOR_USUARIO = '01'
CODE_FINANCIADOR_SIS = '02'
CODE_FINANCIADOR_ESSALUD = '03'
CODE_FINANCIADOR_SOAT = '04'
CODE_FINANCIADOR_SANIDAD_FAP = '05'
CODE_FINANCIADOR_SANIDAD_NAVAL = '06'
CODE_FINANCIADOR_SANIDAD_EP = '07'
CODE_FINANCIADOR_SANIDAD_PNP = '08'
CODE_FINANCIADOR_PRIVADOS = '09'
CODE_FINANCIADOR_OTROS = '10'
CODE_FINANCIADOR_EXONERADO = '11'

STRING_FINANCIADOR_NULO = (CODE_FINANCIADOR_NULO, 'NO SE CONOCE')
STRING_FINANCIADOR_USUARIO = (CODE_FINANCIADOR_USUARIO, 'USUARIO')
STRING_FINANCIADOR_SIS = (CODE_FINANCIADOR_SIS, 'SIS')
STRING_FINANCIADOR_ESSALUD = (CODE_FINANCIADOR_ESSALUD, 'ESSALUD')
STRING_FINANCIADOR_SOAT = (CODE_FINANCIADOR_SOAT, 'SOAT')
STRING_FINANCIADOR_SANIDAD_FAP = (
    CODE_FINANCIADOR_SANIDAD_FAP, 'FINANCIADOR SANIDAD FAP'
)
STRING_FINANCIADOR_SANIDAD_NAVAL = (
    CODE_FINANCIADOR_SANIDAD_NAVAL, 'SANIDAD NAVAL'
)
STRING_FINANCIADOR_SANIDAD_EP = (CODE_FINANCIADOR_SANIDAD_EP, 'SANIDAD EP')
STRING_FINANCIADOR_SANIDAD_PNP = (CODE_FINANCIADOR_SANIDAD_PNP, 'SANIDAD PNP')
STRING_FINANCIADOR_PRIVADOS = (CODE_FINANCIADOR_PRIVADOS, 'PRIVADOS')
STRING_FINANCIADOR_OTROS = (CODE_FINANCIADOR_OTROS, 'OTROS')
STRING_FINANCIADOR_EXONERADO = (CODE_FINANCIADOR_EXONERADO, 'EXONERADO')

SIS_FINANCIADOR_LIST = (
    STRING_FINANCIADOR_NULO, STRING_FINANCIADOR_USUARIO, STRING_FINANCIADOR_SIS,
    STRING_FINANCIADOR_ESSALUD, STRING_FINANCIADOR_SOAT,
    STRING_FINANCIADOR_SANIDAD_FAP, STRING_FINANCIADOR_SANIDAD_NAVAL,
    STRING_FINANCIADOR_SANIDAD_EP, STRING_FINANCIADOR_SANIDAD_PNP,
    STRING_FINANCIADOR_PRIVADOS, STRING_FINANCIADOR_OTROS,
    STRING_FINANCIADOR_EXONERADO
)

CODE_AREA_REHABILITACION = '01'
STRING_AREA_REHABILITACION = (
    CODE_AREA_REHABILITACION, 'Discapacidad y Rehabilitacion'
)
SIS_AREA_LIST = (
    STRING_AREA_REHABILITACION,
)

CODE_MEDICO_MEDICO = '01'
CODE_MEDICO_TECNOLOGO = '02'
STRING_MEDICO_MEDICO = (CODE_MEDICO_MEDICO, 'MEDICO')
STRING_MEDICO_TECNOLOGO = (CODE_MEDICO_TECNOLOGO, 'TECNOLOGO')
SIS_MEDICO_LIST = (
    STRING_MEDICO_MEDICO,
    STRING_MEDICO_TECNOLOGO
)

SEXO_CHOICES = (
    ('01', 'Masculino'),
    ('02', 'Femenino'),
)

ETNIA_CHOICES = (
    ('01', 'AYMARA'),
    ('02', 'URO'),
    ('03', 'JAQARU, KAWI (JAQI, CAUQUI)'),
    ('04', 'CHANCAS'),
    ('05', 'CHOPCCAS'),
    ('06', "Q'EROS"),
    ('07', 'WANCAS'),
    ('08', 'OTROS GRUPOS QUECHUAS DEL AREA ANDINA (II)'),
    ('09', 'ACHUAR, ACHUAL'),
    ('10', 'AMAHUACA'),
    ('11', 'AMAIWERI • KISAMBAERI'),
    ('12', 'AMARA KAERI'),
    ('13', 'ANDOA - SHIMIGAE'),
    ('14', 'ANDOKE'),
    ('15', 'ARABELLA (CHIRUPINO)'),
    ('16', 'ARASAIRE'),
    ('17', 'ASHANINKA'),
    ('18', 'ASHENINKA'),
    ('19', 'AWAJUN (AGUARUNA, AENTS)'),
    ('20', 'BORA (MIAMUNA)'),
    ('21', 'CACATAIBO (UNI)'),
    ('22', 'CAHUARANA (MOROCANO)'),
    ('23', 'CANDOSHI - MURATO'),
    ('24', 'CAPANAHUA (JUNIKUIN)'),
    ('25', 'CAQUINTE (POYENISATI)'),
    ('26', 'CASHINAHUA (JUNIKUIN)'),
    ('27', 'CHAMICURO (CHAMEKOLO)'),
    ('28', 'CHITONAHUA'),
    ('29', 'COCAMA - COCAMILLA'),
    ('30', 'CUJARE—O (I—APARI)'),
    ('31', 'CULINA (MADIJA)'),
    ('32', 'ESE´EJA ("HUARAYO")'),
    ('33', 'HARAKMBUT'),
    ('34', 'HUACHIPAIRE'),
    ('35', 'HUAORANI (TAGAERI, TAROMENANE)'),
    ('36', 'HUITOTO (INCLUYE MURUI, MENECA, MUNAINE)'),
    ('37', 'IQUITO'),
    ('38', 'ISCONAHUA (ICOBAKEBO)'),
    ('39', 'JEBERO (SHIWIIU, SEWELO)'),
    ('40', 'JIBARO'),
    ('41', 'LAMISTO'),
    ('42', 'MACHIGUENGA (MATSIGENKA)'),
    ('43', 'MASHCO - PIRO ("MASHCO")'),
    ('44', 'MASTANAHUA'),
    ('45', 'MAYORUNA (MATS...)'),
    ('46', 'MURUNAHUA'),
    ('47', 'NANTI'),
    ('48', 'NOMATSIGUENGA'),
    ('49', 'OCAINA (IVOT´SA)'),
    ('50', 'OMAGUA'),
    ('51', 'OREJON (MAI HUNA, MAIJUNA)'),
    ('52', 'PISABO (MAYO, KANIBO)'),
    ('53', 'PUKIRIERI'),
    ('54', 'QUICHUA - QUICHUA RUNA, KICHWA (I)'),
    ('55', 'RESIGARO'),
    ('56', 'SAPITERI'),
    ('57', 'SECOYA (AIDO PAI)'),
    ('58', 'CHAPRA'),
    ('59', 'SHARANAHUA / MARINAHUA (ONIKOIN)'),
    ('60', 'SHAWI (CHAYAHUITA, KANPUNAN, KAMPU PIYAWI)'),
    ('61', 'SHIPIBO - CONIBO - SHETEBO'),
    ('62', 'SHUAR'),
    ('63', 'TAUSHIRO (PINCHE)'),
    ('64', 'TICUNA (DU<X<GU)'),
    ('65', 'TOYOERI'),
    ('66', 'URARINA (ITUKALE, SHIMACO, KACH¡)'),
    ('67', 'WAMPIS (HUAMBISA)'),
    ('68', 'YAGUA (YAWA, NIHAMWO)'),
    ('69', 'YAMINAHUA'),
    ('70', 'YANESHA ("AMUESHA")'),
    ('71', 'YINE • YAMI ("PIRO")'),
    ('72', 'YORA ("NAHUA", "PARQUENAHUA")'),
    ('73', 'OTROS GRUPOS INDIGENAS AMAZONICOS'),
    ('80', 'MESTIZO'),
    ('81', 'AFRO DESCENDIENTE'),
    ('82', 'ASIATICO DESCENDIENTE'),
    ('83', 'OTRO')
)

AYUDA_TECNICA_CHOICES = (
    ('01', 'Para terapia y entrenamiento médico básico'),
    ('02', 'Uso de orteticas y protesis'),
    ('03', 'Ayuda relevantes para marcha y transporte'),
    ('04', 'Ayuda para entrenamiento de funciones mentales básicas'),
    ('05', 'Ayuda para comunicación, información y señalización'),
    ('06', 'Ayuda para cocinar y comer'),
    ('07', 'No requiere')
)

ACC_DANIO_CHOICES = (
    ('01', 'Enfermedad Profesional'),
    ('02', 'Accidente de Trabajo'),
    ('03', 'Ninguna de las Anteriores')

)

GRADO_INSTRUCION_CHOICES = (
    ('00', 'NINGUN NIVEL / ILETRADO'),
    ('01', 'INCIAL / PRE-ESCOLAR'),
    ('02', 'PRIMARIA INCOMPLETA'),
    ('03', 'PRIMARIA COMPLETA'),
    ('04', 'ESECUNDARIA INCOMPLETA'),
    ('05', 'SECUNDARIA COMPLETA'),
    ('06', 'SUPERIOR NO UNIV. INC.'),
    ('07', 'SUPERIOR NO UNIV. COMP.'),
    ('08', 'SUPERIOR UNIV. INC.'),
    ('09', 'SUPERIOR UNIV. COMP.')

)

CODE_TIPO_CITA_ATENDIDO = '01'
CODE_TIPO_CITA_ESPERA = '02'
CODE_TIPO_CITA_CANCELADO = '03'
STRING_TIPO_CITA_ATENDIDO = (CODE_TIPO_CITA_ATENDIDO, 'Atendido')
STRING_TIPO_CITA_ESPERA = (CODE_TIPO_CITA_ESPERA, 'En Espera')
STRING_TIPO_CITA_CANCELADO = (CODE_TIPO_CITA_CANCELADO, 'Cancelado')

TIPO_CITA_CHOICES = (
    STRING_TIPO_CITA_ATENDIDO, STRING_TIPO_CITA_ESPERA,
    STRING_TIPO_CITA_CANCELADO
)

CODE_REFERENCIA_NULO = '00'
CODE_REFERENCIA_INICIATIVA_PROPIA = '01'
STRING_REFERENCIA_NULO = (CODE_REFERENCIA_NULO, 'Nulo')
STRING_REFERENCIA_INICIATIVA_PROPIA = (
CODE_REFERENCIA_INICIATIVA_PROPIA, 'Iniciativa Propia'
)
TIPO_REFERENCIA = (
    STRING_REFERENCIA_NULO, STRING_REFERENCIA_INICIATIVA_PROPIA
)
