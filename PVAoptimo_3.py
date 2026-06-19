from opentrons import protocol_api
from opentrons.protocol_api import SINGLE
from opentrons.types import Point

metadata = {
    'protocolName': 'Sintesis Automatizada de Hidrogeles PVA-PEGDA-LAP (terceras 32-3 rep) optimizado (LHS Design)',
    'author': 'NicoPeña',
    'description': 'Preparacion de 96 muestras con gradientes de PEGDA, PVA y LAP usando Latin Hypercube Sampling.',
}

requirements = {"robotType": "Flex", "apiLevel": "2.21"}

def run(protocol: protocol_api.ProtocolContext):
    
    muestras = [
    ["A1", 70.00, 90.00], ["A2", 32.50, 59.50], ["A3", 67.50, 84.50], ["A4", 20.00, 44.00],
    ["A5", 45.00, 55.00], ["A6", 60.00, 20.00], ["A7", 55.00, 25.00], ["A8", 25.00, 79.00],
    ["A9", 32.50, 51.50], ["A10", 40.00, 32.00], ["A11", 42.50, 45.50], ["A12", 20.00, 44.00],
    ["B1", 65.00, 67.00], ["B2", 65.00, 67.00], ["B3", 55.00, 25.00], ["B4", 50.00, 34.00],
    ["B5", 45.00, 95.00], ["B6", 40.00, 100.00], ["B7", 60.00, 28.00], ["B8", 52.50, 48.83],
    ["B9", 50.00, 34.00], ["B10", 27.50, 100.50], ["B11", 32.50, 59.50], ["B12", 40.00, 38.67],
    ["C1", 35.00, 89.00], ["C2", 37.50, 70.50], ["C3", 37.50, 74.50], ["C4", 40.00, 100.00],
    ["C5", 70.00, 90.00], ["C6", 40.00, 38.67], ["C7", 32.50, 51.50], ["C8", 37.50, 70.50],
    ["C9", 60.00, 20.00], ["C10", 42.50, 45.50], ["C11", 30.00, 82.00], ["C12", 35.00, 89.00],
    ["D1", 50.00, 34.00], ["D2", 22.50, 53.50], ["D3", 52.50, 48.83], ["D4", 60.00, 20.00],
    ["D5", 22.50, 53.50], ["D6", 52.50, 48.83], ["D7", 40.00, 38.67], ["D8", 30.00, 82.00],
    ["D9", 47.50, 48.50], ["D10", 42.50, 45.50], ["D11", 52.50, 67.50], ["D12", 55.00, 25.00],
    ["E1", 37.50, 70.50], ["E2", 60.00, 28.00], ["E3", 32.50, 59.50], ["E4", 42.50, 36.17],
    ["E5", 32.50, 59.50], ["E6", 42.50, 33.50], ["E7", 50.00, 24.67], ["E8", 42.50, 36.17],
    ["E9", 30.00, 102.00], ["E10", 37.50, 30.50], ["E11", 47.50, 48.50], ["E12", 45.00, 55.00],
    ["F1", 37.50, 30.50], ["F2", 65.00, 67.00], ["F3", 35.00, 89.00], ["F4", 52.50, 67.50],
    ["F5", 45.00, 95.00], ["F6", 60.00, 28.00], ["F7", 30.00, 102.00], ["F8", 25.00, 79.00],
    ["F9", 50.00, 24.67], ["F10", 47.50, 48.50], ["F11", 50.00, 24.67], ["F12", 40.00, 100.00],
    ["G1", 22.50, 53.50], ["G2", 37.50, 30.50], ["G3", 27.50, 100.50], ["G4", 42.50, 33.50],
    ["G5", 52.50, 67.50], ["G6", 37.50, 74.50], ["G7", 67.50, 84.50], ["G8", 40.00, 32.00],
    ["G9", 70.00, 90.00], ["G10", 37.50, 74.50], ["G11", 45.00, 55.00], ["G12", 42.50, 36.17],
    ["H1", 25.00, 79.00], ["H2", 20.00, 44.00], ["H3", 32.50, 59.50], ["H4", 40.00, 32.00],
    ["H5", 32.50, 59.50], ["H6", 30.00, 82.00], ["H7", 32.50, 51.50], ["H8", 30.00, 102.00],
    ["H9", 45.00, 95.00], ["H10", 67.50, 84.50], ["H11", 27.50, 100.50], ["H12", 42.50, 33.50]
    ]
        
    m_pva_10 = [
    ["A1", 20.00], ["A2", 40.00], ["A3", 20.00], ["A4", 60.00],
    ["A6", 80.00], ["A7", 40.00], ["A8", 20.00], ["A9", 80.00],
    ["A10", 80.00], ["A11", 40.00], ["A12", 60.00], ["B1", 20.00],
    ["B2", 20.00], ["B3", 40.00], ["B5", 0.00], ["B6", 20.00],
    ["B7", 40.00], ["B10", 40.00], ["B11", 40.00], ["C1", 20.00],
    ["C2", 40.00], ["C3", 40.00], ["C4", 20.00], ["C5", 20.00],
    ["C7", 80.00], ["C8", 40.00], ["C9", 80.00], ["C10", 40.00],
    ["C11", 40.00], ["C12", 20.00], ["D2", 80.00], ["D4", 80.00],
    ["D5", 80.00], ["D8", 40.00], ["D10", 40.00], ["D11", 20.00],
    ["D12", 40.00], ["E1", 40.00], ["E2", 40.00], ["E3", 40.00],
    ["E5", 40.00], ["E9", 40.00], ["E10", 80.00], ["F1", 80.00],
    ["F2", 20.00], ["F3", 20.00], ["F4", 20.00], ["F5", 0.00],
    ["F6", 40.00], ["F7", 40.00], ["F8", 20.00], ["F12", 20.00],
    ["G1", 80.00], ["G2", 80.00], ["G3", 40.00], ["G5", 20.00],
    ["G6", 40.00], ["G7", 20.00], ["G8", 80.00], ["G9", 20.00],
    ["G10", 40.00], ["H1", 20.00], ["H2", 60.00], ["H3", 40.00],
    ["H4", 80.00], ["H5", 40.00], ["H6", 40.00], ["H7", 80.00],
    ["H8", 40.00], ["H9", 0.00], ["H10", 20.00], ["H11", 40.00]
    ]

    m_pva_15 = [
        ["A5", 80.00], ["B4", 40.00], ["B8", 66.67], ["B9", 40.00],
        ["B12", 53.33], ["C6", 53.33], ["D1", 40.00], ["D3", 66.67],
        ["D6", 66.67], ["D7", 53.33], ["D9", 80.00], ["E4", 53.33],
        ["E6", 80.00], ["E7", 93.33], ["E8", 53.33], ["E11", 80.00],
        ["E12", 80.00], ["F9", 93.33], ["F10", 80.00], ["F11", 93.33],
        ["G4", 80.00], ["G11", 80.00], ["G12", 53.33], ["H12", 80.00]
    ]
    
    m_lap_05 = [
    ["A1", 20.00], ["A2", 68.00], ["A3", 28.00], ["A4", 76.00],
    ["A5", 20.00], ["A6", 40.00], ["A7", 80.00], ["A8", 76.00],
    ["A9", 36.00], ["A10", 48.00], ["A11", 72.00], ["A12", 76.00],
    ["B1", 48.00], ["B2", 48.00], ["B3", 80.00], ["B4", 76.00],
    ["B5", 60.00], ["B6", 40.00], ["B7", 72.00], ["B8", 32.00],
    ["B9", 76.00], ["B10", 32.00], ["B11", 68.00], ["B12", 68.00],
    ["C1", 56.00], ["C2", 52.00], ["C3", 48.00], ["C4", 40.00],
    ["C5", 20.00], ["C6", 68.00], ["C7", 36.00], ["C8", 52.00],
    ["C9", 40.00], ["C10", 72.00], ["C11", 48.00], ["C12", 56.00],
    ["D1", 76.00], ["D2", 44.00], ["D3", 32.00], ["D4", 40.00],
    ["D5", 44.00], ["D6", 32.00], ["D7", 68.00], ["D8", 48.00],
    ["D9", 24.00], ["D10", 72.00], ["D11", 60.00], ["D12", 80.00],
    ["E1", 52.00], ["E2", 72.00], ["E3", 68.00], ["E4", 68.00],
    ["E5", 68.00], ["E6", 44.00], ["E8", 68.00], ["E9", 28.00],
    ["E10", 52.00], ["E11", 24.00], ["E12", 20.00], ["F1", 52.00],
    ["F2", 48.00], ["F3", 56.00], ["F4", 60.00], ["F5", 60.00],
    ["F6", 72.00], ["F7", 28.00], ["F8", 76.00], ["F10", 24.00],
    ["F12", 40.00], ["G1", 44.00], ["G2", 52.00], ["G3", 32.00],
    ["G4", 44.00], ["G5", 60.00], ["G6", 48.00], ["G7", 28.00],
    ["G8", 48.00], ["G9", 20.00], ["G10", 48.00], ["G11", 20.00],
    ["G12", 68.00], ["H1", 76.00], ["H2", 76.00], ["H3", 68.00],
    ["H4", 48.00], ["H5", 68.00], ["H6", 48.00], ["H7", 36.00],
    ["H8", 28.00], ["H9", 60.00], ["H10", 28.00], ["H11", 32.00],
    ["H12", 44.00]
    ]

    m_lap_1 = [
        ["E7", 32.00], ["F9", 32.00], ["F11", 32.00]
    ]

    # --- 1. CARGA DE LABWARE ---
    trash = protocol.load_trash_bin("A3")
    tipracks = protocol.load_labware("opentrons_flex_96_tiprack_200ul", "D3")
    res = protocol.load_labware("custom_4_reservoir_90000ul", "D2")
    res_lapeg = protocol.load_labware("19mlglass_15_tuberack_19000ul", "B2")
    h_s = protocol.load_module('heaterShakerModuleV1', 'C1') 
    plate = h_s.load_labware("corning_96_wellplate_360ul_flat")

    # --- 2. PIPETTE ---
    pipette = protocol.load_instrument("flex_8channel_1000", mount="left", tip_racks=[tipracks])
    pipette.configure_nozzle_layout(style=SINGLE, start="H1")

    # --- 3. SEGURIDAD: CERRAR LATCH ---
    h_s.close_labware_latch()

    # --- 4. REACTIVOS ---
    pegda_80 = res_lapeg['C1']
    agua = res['A1']
    pva_10 = res_lapeg['B1']
    pva_15 = res_lapeg['B2']
    lap_05 = res_lapeg['A1']
    lap_1 = res_lapeg['A2']

    vol_max_p200 = 190

    #PASO 1: AGUA
    protocol.comment("Distribuyendo Agua...")
    pipette.flow_rate.aspirate = 80
    pipette.flow_rate.dispense = 30
    pipette.flow_rate.blow_out = 60
    
    pipette.pick_up_tip(tipracks['A1'])
    for well, v_peg, v_agua in muestras:
        pipette.aspirate(v_agua, agua.bottom(z=3))
        pipette.dispense(v_agua, plate[well].top(z=2))
        dest_pared = plate[well].top(z=-2).move(Point(x=0, y=-2.5, z=0))
        pipette.move_to(dest_pared, speed=10) 
        pipette.blow_out(dest_pared)
        pipette.move_to(plate[well].top(z=10))
        protocol.delay(seconds=1)
    pipette.drop_tip(trash)

    #PASO 2: PVA 10%
    protocol.comment("Distribuyendo PVA 10%...")
    pipette.flow_rate.aspirate = 10
    pipette.flow_rate.dispense = 10
    pipette.flow_rate.blow_out = 30
    pipette.pick_up_tip(tipracks['A2'])
    for well, v_pva in m_pva_10:
        pipette.aspirate(v_pva, pva_10.bottom(z=8))
        protocol.delay(seconds=5) 
        pipette.move_to(pva_10.top(z=5),speed=5)
        pipette.dispense(v_pva, plate[well].top(z=2))
        protocol.delay(seconds=5) 
        dest_pared = plate[well].top(z=-2).move(Point(x=0, y=-2.5, z=0))
        pipette.move_to(dest_pared, speed=10) 
        pipette.blow_out(dest_pared)
        pipette.move_to(plate[well].top(z=10))
        protocol.delay(seconds=1)
    pipette.drop_tip(trash)

    #PASO 3: PVA 15%
    protocol.comment("Distribuyendo PVA 15%...")
    pipette.flow_rate.aspirate = 5
    pipette.flow_rate.dispense = 5
    pipette.flow_rate.blow_out = 20
    pipette.pick_up_tip(tipracks['A3'])
    for well, v_pva in m_pva_15:
        pipette.aspirate(v_pva, pva_15.bottom(z=8))
        protocol.delay(seconds=5) 
        pipette.move_to(pva_15.top(z=5),speed=5)
        pipette.dispense(v_pva, plate[well].top(z=2))
        protocol.delay(seconds=5)
        dest_pared = plate[well].top(z=-2).move(Point(x=0, y=-2.5, z=0))
        pipette.move_to(dest_pared, speed=10) 
        pipette.blow_out(dest_pared)
        protocol.delay(seconds=3)
        pipette.move_to(plate[well].top(z=10))
        protocol.delay(seconds=1)
    pipette.drop_tip(trash)

    #PASO 4: PEGDA
    protocol.comment("Distribuyendo Pegda...")
    pipette.flow_rate.aspirate = 30
    pipette.flow_rate.dispense = 30
    pipette.flow_rate.blow_out = 40
    pipette.pick_up_tip(tipracks['A4'])
    for well, v_peg, v_agua in muestras:
        pipette.aspirate(v_peg, pegda_80.bottom(z=8))
        protocol.delay(seconds=3) 
        pipette.move_to(pegda_80.top(z=5),speed=10)
        pipette.dispense(v_peg, plate[well].top(z=2))
        dest_pared = plate[well].top(z=-2).move(Point(x=0, y=-2.5, z=0))
        pipette.move_to(dest_pared, speed=10) 
        pipette.blow_out(dest_pared)
        pipette.move_to(plate[well].top(z=10))
        protocol.delay(seconds=1)
    pipette.drop_tip(trash)

    #PASO 5: LAP 0.5%
    protocol.comment("Distribuyendo LAP 0.5%...")
    pipette.flow_rate.aspirate = 80
    pipette.flow_rate.dispense = 40
    
    pipette.pick_up_tip(tipracks['A5'])
    liquido_en_punta = 0
    for well, v_lap in m_lap_05:
        if liquido_en_punta < (v_lap + 10):
            espacio_libre = vol_max_p200 - liquido_en_punta
            pipette.aspirate(espacio_libre, lap_05.bottom(z=8))
            liquido_en_punta = vol_max_p200
        pipette.dispense(v_lap, plate[well].top(z=2))
        pipette.touch_tip(v_offset=-3, speed=5)
        protocol.delay(seconds=2)
        liquido_en_punta -= v_lap
    pipette.drop_tip(trash)
    
        # PASO 6: LAP 1%
    protocol.comment("Distribuyendo LAP 1%...")
    pipette.flow_rate.aspirate = 80
    pipette.flow_rate.dispense = 40
    
    pipette.pick_up_tip(tipracks['A6'])
    liquido_en_punta = 0
    for well, v_lap in m_lap_1:
        if liquido_en_punta < (v_lap + 10):
            espacio_libre = vol_max_p200 - liquido_en_punta
            pipette.aspirate(espacio_libre, lap_1.bottom(z=8))
            liquido_en_punta = vol_max_p200
        pipette.dispense(v_lap, plate[well].top(z=2))
        pipette.touch_tip(v_offset=-3, speed=5)
        protocol.delay(seconds=2)
        liquido_en_punta -= v_lap
    pipette.drop_tip(trash)

     # --- 7. FINALIZACIÓN ---
    protocol.comment("Iniciando agitación...")
    h_s.set_and_wait_for_shake_speed(1000)
    protocol.delay(minutes=2)
    h_s.deactivate_shaker()
    h_s.open_labware_latch()
    protocol.comment("Protocolo terminado.")