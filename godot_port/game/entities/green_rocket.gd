extends Area2D


var speed = 200


func _process(delta):
	# Move the rocket towards the mouse
	
	var mouse_pos = get_viewport().get_mouse_position()
	look_at(mouse_pos)
	position += global_transform.x * delta * speed

func _on_PlayerRocket_area_entered(area):
	# Destroy both rockets if they collide
	# Tell the game that the player can spawn another rocket
	# Spawn an explotion
	
	if area.is_in_group("red_rocket"):
		get_node("/root/Game").has_rocket = false
		
		var explotion_scn = load("res://game/entities/explotion.tscn")
		var explotion_inst = explotion_scn.instance()
		get_node("/root/Game").add_child(explotion_inst)
		explotion_inst.global_position = lerp(area.global_position, global_position, 0.5)
		
		area.queue_free()
		queue_free()
