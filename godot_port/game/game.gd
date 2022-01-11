extends Node

#==========Variables===========
var red_health = 100 setget red_health_changed
var green_health = 100 setget green_health_changed

var has_rocket = false
var end_of_game = false

var red_rocket_scn = preload("res://game/entities/red_rocket.tscn")
var green_rocket_scn = preload("res://game/entities/green_rocket.tscn")

#=======Private Functions========
func _ready():
	randomize()

func _process(delta):
	# Move all the red rockets through their paths, if they 
	# reach the end then destroy them and take damange
	
	var rockets = get_tree().get_nodes_in_group("red_rocket")
	for i in rockets.size():
		rockets[i].get_parent().offset += delta * 100
		if rockets[i].get_parent().unit_offset > 0.95:
			rockets[i].get_parent().queue_free()
			self.green_health -= 10
	
	if red_health <= 0:
		end_of_game = true
		$VictoryMenu/won.text = "Green Won"
		$VictoryMenu.visible = true
	if green_health <= 0:
		end_of_game = true
		$VictoryMenu/won.text = "Red Won"
		$VictoryMenu.visible = true
	
	if end_of_game:
		if Input.is_action_just_pressed("ui_select"):
			get_tree().reload_current_scene()

#=======setters========
func green_health_changed(value):
	green_health = value
	$GreenHealth.value = value

func red_health_changed(value):
	red_health = value
	$RedHealth.value = value

#=============signal functions===========
func _on_RocketSpawnRate_timeout():
	if end_of_game: return
	
	var rand_index = randi() % $RedMissilePaths.get_child_count()
	var selected_path = $RedMissilePaths.get_child(rand_index)
	
	# Add the rocket to the path
	var rocket_inst = red_rocket_scn.instance()
	var pathfollow = PathFollow2D.new()
	pathfollow.loop = false
	pathfollow.add_child(rocket_inst)
	selected_path.add_child(pathfollow)
	
	$RocketSpawnRate.wait_time = rand_range(1, 5)
	
func _on_RocketSpawnButton_pressed():
	if not has_rocket:
		# Spawn grene rocket
		has_rocket = true
		var rocket_inst = green_rocket_scn.instance()
		add_child(rocket_inst)
		rocket_inst.global_position = $GreenArea/CollisionShape2D.position

func _on_RedArea_area_entered(area):
	# Give damage if hit red base
	if area.is_in_group("green_rocket"):
		self.red_health -= 10
		area.queue_free()
		has_rocket = false



