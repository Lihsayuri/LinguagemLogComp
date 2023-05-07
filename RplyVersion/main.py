
from parserling import Parser
from lexerling import Lexer

text_input = """ ITS LIGHTS OUT AND AWAY WE GO 
driver piloto1 is 'Leclerc'
driver_engineer engenheiro_piloto1 is 'Martin Whitmarsh'
team time_piloto1 is 'Ferrari'
grand_prix corrida is 'Bahrain'
expected_sc SC is False
rain_probability chance_chuva is 0.2
drs_usage uso_drs is (sector1, 3)
aggressive_overtaking agressivo is (31,50)
conservative_overtaking conservador is (1,28)
sets_of_tyres conjunto is {{soft, fresh}, {medium, fresh}, {hard, fresh}, {medium, lil_used}}
lap voltas is 0
tyre pneu_atual is {soft, fresh}
SetUp Pitstop need tyre pneu, driver piloto
Radio_on
radio_check typeof.pneu is soft then >> typeof.pneu is medium and statusof.pneu is lil_used -Copy!
radio_check typeof.pneu is medium and statusof.pneu is lil_used then >> typeof.pneu is hard and statusof.pneu is fresh -Copy!
radio_check typeof.pneu is hard then >> typeof.pneu is medium and statusof.pneu is fresh -Copy!
Radio_off
SetUp expectedRain need rain_probability chance_of_rain, conservative_overtaking coservador
Radio_on
radio_check chance_of_rain is 0.2 then >> conservador is (1,20) -Copy!
no_response >> conservador is (1,30) -Copy!
Radio_off
SetUp use_DRS need drs_usage uso_drs, lap voltas, aggressive_overtaking agressivo
Radio_on
radio_check uso_drs > 0 and voltas in agressivo then >> availabilityof.uso_drs is availabilityof.uso_drs-1 -Copy!
Radio_off
EngineOn[voltas]
radio_check voltas is 10 then >> call Pitstop need tyre pneu_atual, driver piloto1 -Copy!
radio_check voltas is 16 then >> call use_DRS need drs_usage uso_drs, lap voltas, aggressive_overtaking agressivo -Copy!
radio_check voltas is 21 then >> call Pitstop need tyre pneu_atual, driver piloto1 -Copy!
radio_check voltas is 41 then >> call Pitstop need tyre pneu_atual, driver piloto1 -Copy!
radio_check voltas is 42 then >> call use_DRS need drs_usage uso_drs, lap voltas, aggressive_overtaking agressivo -Copy!
radio_check voltas is 45 then >> call use_DRS need drs_usage uso_drs, lap voltas, aggressive_overtaking agressivo -Copy!
EngineOff
CHECKRED FLAG"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
# parser.parse(tokens).eval()
parser.parse(tokens)

for token in tokens:
    print(token)