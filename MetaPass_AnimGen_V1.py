import bpy

def GenerateAnim(hero_text, ticket_no,venue,date, ImageLocation):
    
    #select and change HeroText
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = None
    HeroText = bpy.data.objects['HeroText']
    bpy.context.view_layer.objects.active = HeroText
    HeroText.select_set(True)        
    HeroText.data.body = hero_text
    
    #select and change TicketNumber
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = None
    TicketNumber = bpy.data.objects['TicketNumber']
    bpy.context.view_layer.objects.active = TicketNumber
    TicketNumber.select_set(True)
    TicketNumber.data.body = ticket_no
    
    #select and change Date
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = None
    Date = bpy.data.objects['Date']
    bpy.context.view_layer.objects.active = Date
    Date.select_set(True)
    Date.data.body = date
    
    #select and change Venue
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = None
    Venue = bpy.data.objects['Venue']
    bpy.context.view_layer.objects.active = Venue
    Venue.select_set(True)
    Venue.data.body = venue
    
    #setup Image
    ImageNode = bpy.data.materials["ImageMat"].node_tree.nodes["BGImage"]
    img = bpy.data.images.load(ImageLocation)
    if img:
        ImageNode.image = img
    
    #render stuff
    bpy.ops.render.render(animation=True, use_viewport=True)
    




GenerateAnim('Farhan','007', 'Lisbon', 'May 1', '//Refs\\2.png')
